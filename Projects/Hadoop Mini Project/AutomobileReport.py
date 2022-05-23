from mrjob.job import MRJob
from mrjob.step import MRStep

class AutoBreakdown(MRJob):
    def mapper(self, _, line):
        incident_id, incident_type, vin_number, make, model, year, incident_date, description = line.split(',')
        yield vin_number, [incident_type, make, year]
    
    def reducer(self, key, values):
        make = ""
        year = ""
        for v in values:
            if v[0] == "I":
                make = v[1]
                year = v[2]
            if v[0] == "A":
                v[1] = make
                v[2] = year
                yield key, v

if __name__ == '__main__':
    AutoBreakdown.run()