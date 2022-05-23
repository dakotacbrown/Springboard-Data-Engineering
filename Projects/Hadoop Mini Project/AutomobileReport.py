from mrjob.job import MRJob
from mrjob.step import MRStep

class AutoBreakdown(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_vins,
                   reducer=self.reducer_find_make_year)
        ]

    def mapper_get_vins(self, _, line):
        (incident_id, incident_type, vin_number, make, model, year, incident_date, description) = line.split(',')
        yield (vin_number, [incident_type, make, year])

    def reducer_find_mak_year(self, key, values):
        yield (key, [values.make, values.year]) 

if __name__ == '__main__':
    AutoBreakdown.run()