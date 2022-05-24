from mrjob.job import MRJob
from mrjob.step import MRStep

class AutoBreakdown(MRJob):
    def steps(self):
        return [
            MRStep(
                mapper=self.mapper_1,
                reducer=self.reducer_1
            ),
            MRStep(
                mapper=self.mapper_2,
                reducer=self.reducer_2
            )
        ]

    def mapper_1(self, _, line):
        _, incident_type, vin_number, make, _, year, _, _ = line.split(',')
        yield vin_number, [incident_type, make, year]
    
    def reducer_1(self, key, values):
        make = ""
        year = ""

        for v in values:
            if v[0] == "I":
                make = v[1]
                year = v[2]
                break

        for v in values:
            if v[0] =="A":
                yield key, [make, year]
    
    def mapper_2(self, _, line):
        make, year = line
        yield [make, year], 1

    
    def reducer_2(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    AutoBreakdown.run()