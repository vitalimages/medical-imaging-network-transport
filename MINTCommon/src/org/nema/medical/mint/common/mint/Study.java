
package org.nema.medical.mint.common.mint;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

import com.vitalimages.contentserver.mint.Mint2Gpb.AttributeData;
import com.vitalimages.contentserver.mint.Mint2Gpb.SeriesData;
import com.vitalimages.contentserver.mint.Mint2Gpb.StudyData;

/**
 * Schema fragment(s) for this class:
 * <pre>
 * &lt;xs:complexType xmlns:ns="http://vitalimages.com/contentserver/mint" xmlns:xs="http://www.w3.org/2001/XMLSchema" name="StudyMetaType">
 *   &lt;xs:sequence>
 *     &lt;xs:element type="ns:AttributesType" name="Attributes" minOccurs="1" maxOccurs="1"/>
 *     &lt;xs:element type="ns:SeriesListType" name="SeriesList"/>
 *   &lt;/xs:sequence>
 *   &lt;xs:attribute type="xs:string" use="required" name="studyInstanceUID"/>
 * &lt;/xs:complexType>
 * </pre>
 */
public class Study implements AttributeStore
{
    private final Map<Integer,Attribute> attributeMap = new HashMap<Integer,Attribute>();
    private final Map<String,Series> seriesMap = new HashMap<String,Series>();
    private String studyInstanceUID;

    /**
     * @param tag
     * @return the attribute for the given tag
     */
    public Attribute getAttribute(final int tag) {
        return attributeMap.get(tag);
    }

    public String getValueForAttribute(final int tag) {
        Attribute attr = getAttribute(tag);
        return attr != null ? attr.getVal() : null;
    }

    /**
     * puts an Attribute into the Series - attributes are unique per tag
     * @param attr
     */
    public void putAttribute(final Attribute attr) {
        attributeMap.put(attr.getTag(), attr);
    }

    /**
     * removes the Attribute with the given tag from the Series
     * @param tag
     */
    public void removeAttribute(final int tag) {
        attributeMap.remove(tag);
    }

    /**
     * @return an iterator of all Attributes in the Series
     */
    public Iterator<Attribute> attributeIterator() {
        return attributeMap.values().iterator();
    }

    /**
     * @param uid
     * @return the series for the given uid
     */
    public Series getSeries(final String uid) {
        return seriesMap.get(uid);
    }

    /**
     * puts an Series into the Study - series are unique per uid
     * @param attr
     */
    public void putSeries(final Series series) {
        seriesMap.put(series.getSeriesInstanceUID(), series);
    }

    /**
     * removes the Series with the given uid from the Study
     * @param uid
     */
    public void removeSeries(final String uid) {
        seriesMap.remove(uid);
    }

    /**
     * @return an iterator of all Series in the Study
     */
    public Iterator<Series> seriesIterator() {
        return seriesMap.values().iterator();
    }

    /**
     * Get the 'studyInstanceUID' attribute value.
     *
     * @return value
     */
    public String getStudyInstanceUID() {
        return studyInstanceUID;
    }

    /**
     * Set the 'studyInstanceUID' attribute value.
     *
     * @param studyInstanceUID
     */
    public void setStudyInstanceUID(String studyInstanceUID) {
        this.studyInstanceUID = studyInstanceUID;
    }

    //  Google Protocol Buffer support - package protection intentional
    //  Google Protocol Buffer support
    //
    static Study fromGPB(StudyData studyData) {
        Study study = new Study();
        study.setStudyInstanceUID(studyData.getStudyInstanceUid());
        for (AttributeData attrData : studyData.getAttributesList()) {
            Attribute attr = Attribute.fromGPB(attrData);
            study.putAttribute(attr);
        }
        for (SeriesData seriesData : studyData.getSeriesList()) {
            Series series = Series.fromGPB(seriesData);
            study.putSeries(series);
        }
        return study;
    }

    StudyData toGPB() {
        StudyData.Builder builder = StudyData.newBuilder();
        if (this.studyInstanceUID != null) {
        	builder.setStudyInstanceUid(this.studyInstanceUID);
        }
        for (Attribute attr : this.attributeMap.values()) {
            builder.addAttributes(attr.toGPB());
        }
        for (Series series: this.seriesMap.values()) {
            builder.addSeries(series.toGPB());
        }
        StudyData data = builder.build();
        return data;
    }

}
