from pssh.clients import ParallelSSHClient

from utils import read_hosts

COMMAND = 'uname'
HOSTS_FILE = 'hosts.txt'


def main() -> None:
    hosts = read_hosts(HOSTS_FILE)
    client = ParallelSSHClient(hosts)

    output = client.run_command(COMMAND)
    for host_output in output:
        for line in host_output.stdout:
            print(line)


if __name__ == '__main__':
    main()
