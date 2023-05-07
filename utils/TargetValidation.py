import ipaddress
import furl
import re
import validators
import socket


def is_valid_network_block(block):
    try:
        ipaddress.ip_network(block, strict=False)
        return True
    except ValueError:
        return False
    

def is_valid_ip_address(addr):
    if addr.startswith('[') and addr.endswith(']'):
        addr = host[1:-1]
    if validators.ipv4(addr) or validators.ipv6(addr):
        return True
    return False


def is_valid_host(host):
    if host.startswith('[') and host.endswith(']'):
        host = host[1:-1]
    try:
        socket.gethostbyname(host)
        return True
    except socket.error:
        if validators.ipv4(host) or validators.ipv6(host):
            return True
        return False


def is_valid_port(port):
    if port is None:
        return True
    try:
        if 1 <= int(port) <= 65535:
            return True
        else:
            return False
    except ValueError:
        return False


def is_valid_path(path):
    pattern = r'^\/[^\s]+$'
    if re.match(pattern, str(path)) or str(path) == '':
        if not '//' in str(path):
            return True
    return False


def is_valid_query(query):
    if query is None:
        return True
    if not isinstance(query, str):
        return False
    query = query.strip()
    if not query or query.startswith('?') or ' ' in query:
        return False
    return True


def is_valid_fragment(fragment):
    if fragment:
        fragment = str(fragment).strip()
        if len(fragment) == 0 or fragment.startswith('#') or ' ' in fragment:
            return False
        return True
    return False


def is_valid_domain(url):
    try:
        # Base case: empty URL is invalid
        if not url:
            return False
        # Parse the URL using furl
        parsed_url = furl.furl(url)
        # Check the validity of the scheme
        if not parsed_url.scheme:
            return False
        # Check the validity of the host
        if not is_valid_host(parsed_url.host):
            return False
        # Check the validity of the port
        if parsed_url.port and not is_valid_port(parsed_url.port):
            return False
        # Check the validity of the path
        if parsed_url.path and not is_valid_path(parsed_url.path):
            return False
        # Check the validity of the query
        if parsed_url.query and not parsed_url.path:
            if not is_valid_query(parsed_url.query):
                return False
        # Check the validity of the fragment
        if parsed_url.fragment and not parsed_url.path:
            if not is_valid_fragment(parsed_url.fragment):
                return False
        # If all checks pass, the URL is valid
        return True
    except ValueError:
        return False
    