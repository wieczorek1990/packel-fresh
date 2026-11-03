from pssh.clients import ParallelSSHClient

COMMAND = 'uname'
HOSTS_FILE = 'hosts.txt'


def get_hosts(file_path):
    with open(file_path) as file:
        return [line.strip() for line in file if line.strip()]


def main():
    hosts = get_hosts(HOSTS_FILE)
    client = ParallelSSHClient(hosts)

    output = client.run_command(COMMAND)
    for host_output in output:
        for line in host_output.stdout:
            print(line)
        host_output.exit_code


if __name__ == '__main__':
    main()
