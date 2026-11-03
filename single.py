from pssh.clients import SSHClient

COMMAND = 'uname'
HOSTS_FILE = 'host.txt'


def get_host(file_path):
    with open(file_path) as file:
        for line in file:
            line = line.strip()
            if line:
                return line
    return ''


def main():
    host = get_host(HOSTS_FILE)
    client = SSHClient(host)

    host_out = client.run_command(COMMAND)
    for line in host_out.stdout:
        print(line)
    host_out.exit_code


if __name__ == '__main__':
    main()
