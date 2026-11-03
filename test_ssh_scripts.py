import os
import tempfile

from utils import read_hosts, read_single_host


class TestReadHosts:
    """Tests for utils.py's read_hosts function."""

    def test_reads_hosts_from_file(self):
        """Should return a list of hosts from a file."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write("host1\nhost2\nhost3\n")
            f.flush()
            hosts = read_hosts(f.name)
        os.unlink(f.name)

        assert hosts == ["host1", "host2", "host3"]

    def test_strips_whitespace(self):
        """Should strip leading and trailing whitespace from each host."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write("  host1  \n\thost2\t\n host3 \n")
            f.flush()
            hosts = read_hosts(f.name)
        os.unlink(f.name)

        assert hosts == ["host1", "host2", "host3"]

    def test_ignores_empty_lines(self):
        """Should skip empty and whitespace-only lines."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write("host1\n\n   \nhost2\n\n")
            f.flush()
            hosts = read_hosts(f.name)
        os.unlink(f.name)

        assert hosts == ["host1", "host2"]

    def test_single_host(self):
        """Should work with a single host in the file."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write("localhost\n")
            f.flush()
            hosts = read_hosts(f.name)
        os.unlink(f.name)

        assert hosts == ["localhost"]

    def test_file_not_found(self):
        """Should raise FileNotFoundError for missing files."""
        try:
            read_hosts("nonexistent_file.txt")
            assert False, "Expected FileNotFoundError"
        except FileNotFoundError:
            pass


class TestReadSingleHost:
    """Tests for utils.py's read_single_host function."""

    def test_reads_single_host(self):
        """Should return a single host string from a file."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write("localhost\n")
            f.flush()
            host = read_single_host(f.name)
        os.unlink(f.name)

        assert host == "localhost"

    def test_strips_whitespace(self):
        """Should strip leading and trailing whitespace."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write("  localhost  \n")
            f.flush()
            host = read_single_host(f.name)
        os.unlink(f.name)

        assert host == "localhost"

    def test_file_not_found(self):
        """Should raise FileNotFoundError for missing files."""
        try:
            read_single_host("nonexistent_file.txt")
            assert False, "Expected FileNotFoundError"
        except FileNotFoundError:
            pass

    def test_reads_only_first_line(self):
        """Should return only the first non-empty line when multiple lines exist."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write("localhost\nlocalhost\n")
            f.flush()
            host = read_single_host(f.name)
        os.unlink(f.name)

        assert host == "localhost"

    def test_skips_empty_lines_at_start(self):
        """Should skip empty lines and return the first non-empty line."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write("\n   \nlocalhost\n")
            f.flush()
            host = read_single_host(f.name)
        os.unlink(f.name)

        assert host == "localhost"

    def test_empty_file_returns_empty_string(self):
        """Should return an empty string for an empty file."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write("")
            f.flush()
            host = read_single_host(f.name)
        os.unlink(f.name)

        assert host == ""
