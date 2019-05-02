from elasticsearch import Elasticsearch
import curator

es = Elasticsearch([{'host': 'logstash'}])
def delete_indices(index, days):
    """ Delete indices older than X days """
    ilo = curator.IndexList(es)
    ilo.filter_by_regex(kind="prefix", value=index)
    ilo.filter_by_age(source="creation_date", direction="older", unit="days", unit_count=days)
    delete = curator.DeleteIndices(ilo, master_timeout=900)
    try:
        delete.do_action()
        print("Removed ",index," indices older than ",str(days)," days old.")
    except curator.NoIndices:
        print("No ",index," available for removal.")

if __name__ == '__main__':
    delete_indices("beats-index*", 60)
    delete_indices("gelf-index*", 45)
    delete_indices("wineventlog-index*", 30)
    delete_indices("netflow-index*", 1)
    delete_indices("syslog-index*", 60)
