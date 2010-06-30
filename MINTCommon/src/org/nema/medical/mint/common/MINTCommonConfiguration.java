package org.nema.medical.mint.common;

import java.io.IOException;
import java.util.Properties;

import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingException;
import javax.sql.DataSource;

import org.apache.commons.dbcp.BasicDataSource;
import org.hibernate.SessionFactory;
import org.springframework.context.annotation.Bean;
import org.springframework.core.io.ClassPathResource;
import org.springframework.jndi.JndiObjectFactoryBean;
import org.springframework.orm.hibernate3.HibernateTransactionManager;
import org.springframework.orm.hibernate3.annotation.AnnotationSessionFactoryBean;
import org.springframework.transaction.support.AbstractPlatformTransactionManager;

public abstract class MINTCommonConfiguration {

	protected static HibernateTransactionManager hibernateTransactionManager = null;

	protected static SessionFactory sessionFactory = null;

	protected Context envContext = null;

	protected Properties properties = null;

	public Properties envSpecificProperties() {
		if (properties == null) {
			properties = new Properties();
			final ClassPathResource classPathResource = new ClassPathResource("jdbc.properties");
			try {
				properties.load(classPathResource.getInputStream());
			} catch (final IOException e) {
			}
		}
		return properties;
	}

	protected String getFromContext(final String name) {
		if (name != null) {
			try {
				if (envContext == null) {
					envContext = (Context) new InitialContext().lookup("java:");
				}
				final Object object = envContext.lookup(name);
				if (object != null) {
					return object.toString();
				}
			} catch (final NamingException e) {
			}
		}
		return null;
	}

	protected String getFromContextOrEnvironment(final String name) {
		if (name == null) {
			return null;
		}
		final String context = getFromContext(name);
		if (context != null) {
			return context;
		}
		return System.getenv(name);
	}

	protected String getFromEnvironmentOrProperties(final String name) {
		if (name == null) {
			return null;
		}
		final String environment = getFromContextOrEnvironment(name);
		if (environment != null) {
			return environment;
		}
		return envSpecificProperties().getProperty(name);
	}

	protected String[] getPackagesToScan() {
		return new String[] { "com.vitalimages.contentserver.domain" };
	}

	@Bean(destroyMethod = "close")
	public SessionFactory sessionFactory() throws Exception {
		if (sessionFactory == null) {
			final AnnotationSessionFactoryBean annotationSessionFactoryBean = new AnnotationSessionFactoryBean();

			if (null != getFromEnvironmentOrProperties("hibernate.connection.datasource")) {
				// Using a JNDI dataSource
				final JndiObjectFactoryBean jndiObjectFactoryBean = new JndiObjectFactoryBean();
				jndiObjectFactoryBean.setExpectedType(DataSource.class);
				jndiObjectFactoryBean.setJndiName(getFromEnvironmentOrProperties("hibernate.connection.datasource"));
				jndiObjectFactoryBean.afterPropertiesSet();
				annotationSessionFactoryBean.setDataSource((DataSource) jndiObjectFactoryBean.getObject());
			} else {
				// Not using JNDI data source
				final BasicDataSource dataSource = new BasicDataSource();
				dataSource.setDriverClassName(getFromEnvironmentOrProperties("hibernate.connection.driver_class"));
				dataSource.setUrl(getFromEnvironmentOrProperties("hibernate.connection.url"));
				dataSource.setUsername(getFromEnvironmentOrProperties("hibernate.connection.username"));
				dataSource.setPassword(getFromEnvironmentOrProperties("hibernate.connection.password"));
				annotationSessionFactoryBean.setDataSource(dataSource);
			}

			final Properties hibernateProperties = new Properties();
			hibernateProperties.put("hibernate.connection.autocommit", Boolean.TRUE);

			final String dialect = getFromEnvironmentOrProperties("hibernate.dialect");
			if (null != dialect) {
				hibernateProperties.put("hibernate.dialect", dialect);
			}

			final String hbm2dll = getFromEnvironmentOrProperties("hibernate.hbm2ddl.auto");
			hibernateProperties.put("hibernate.hbm2ddl.auto", hbm2dll == null ? "verify" : hbm2dll);

			hibernateProperties.put("hibernate.show_sql", "true"
					.equalsIgnoreCase(getFromEnvironmentOrProperties("hibernate.show_sql")));

			hibernateProperties.put("hibernate.c3p0.max_statement", 50);
			hibernateProperties.put("hibernate.c3p0.maxPoolSize", 20);
			hibernateProperties.put("hibernate.c3p0.minPoolSize", 5);
			hibernateProperties.put("hibernate.c3p0.testConnectionOnCheckout", Boolean.FALSE);
			hibernateProperties.put("hibernate.c3p0.timeout", 600);
			annotationSessionFactoryBean.setHibernateProperties(hibernateProperties);

			annotationSessionFactoryBean.setPackagesToScan(getPackagesToScan());
			annotationSessionFactoryBean.afterPropertiesSet();

			sessionFactory = annotationSessionFactoryBean.getObject();
		}
		return sessionFactory;
	}

	@Bean
	public HibernateTransactionManager transactionManager() throws Exception {
		if (hibernateTransactionManager == null) {
			hibernateTransactionManager = new HibernateTransactionManager();
			hibernateTransactionManager.setSessionFactory(sessionFactory());
			hibernateTransactionManager
					.setTransactionSynchronization(AbstractPlatformTransactionManager.SYNCHRONIZATION_ON_ACTUAL_TRANSACTION);
			hibernateTransactionManager.afterPropertiesSet();
		}
		return hibernateTransactionManager;
	}

}
