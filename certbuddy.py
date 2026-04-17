from Applier.tencent import Tencent
from Deployer.qiniu_ import Qiniu


class CertBuddy:
    def __init__(self):
        self.applier = Tencent()
        self.deployer = Qiniu()

        self.joblist = self.get_joblist()
        print(self.joblist)

    @staticmethod
    def get_joblist():
        with open('.joblist') as f:
            job_data = f.read()
        joblist = job_data.strip().split('\n')
        joblist = list(filter(lambda x: '%' not in x, joblist))
        return joblist

    def run(self):
        for domain in self.joblist:
            try:
                print(f'Processing {domain}')
                print('Applying certificate...')
                certificate = self.applier.apply(domain)
                print('Uploading certificate...')
                self.deployer.deploy(certificate)
            except Exception as e:
                print(f'Failed to process {domain}: {e}')


cb = CertBuddy()
cb.run()
