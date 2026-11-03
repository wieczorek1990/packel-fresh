from pssh.clients import SSHClient

from utils import read_single_host

COMMAND = 'uname'
HOSTS_FILE = 'host.txt'


def main() -> None:
    host = read_single_host(HOSTS_FILE)
    client = SSHClient(host)

    host_out = client.run_command(COMMAND)
    for line in host_out.stdout:
        print(line)


if __name__ == '__main__':
    main()
