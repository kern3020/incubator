import boto.ec2
import boto.iam

'''Bcbio now runs on AWS. This script can help you understand if this
are setup correct or troubleshoot it if there is a problem.
'''

class aws_info(object):
    def __init__(self):
        self._conn = boto.ec2.connect_to_region("us-east-1")

    def print_iam(self):
        print("")
        print ( 
'''Check for IAM. Bcbio needs an IAM user called 'bcbio'. Do you see
it in this list? ''')

        conn = boto.iam.connection.IAMConnection()

        # user
        user_list = conn.get_all_users()
        user_list = user_list[u'list_users_response'][u'list_users_result']['users']
        if user_list: 
            for u in user_list:
                print("\tIAM User: {0}".format(u['user_name']))
        else:
            print("\nIAM User: None.")

    def print_vpc(self):
        print('')
        print(
'''Check for security group. Bcbio needs a security group called
'bcbio'. Do you see it in this list?''')

        # list security groups. 
        group_list = self._conn.get_all_security_groups()
        if group_list:
            for sg in group_list:
                print('\t{0}'.format(sg))
        else:
            print("no security groups.")

    def print_instances(self):
        print('')
        print('''Here is a list of instances. ''')
        res_list = self._conn.get_all_reservations()
        if res_list:
            for inst in res_list:
                print("\ttype: {0}, zone: {1}".format(inst.instance_type, inst.placement))
        else:
            print("\tno instances")

    def status(self):
        self.print_iam()
        self.print_vpc()
        self.print_instances()

if __name__ == "__main__":
    a1 = aws_info()
    a1.status()
