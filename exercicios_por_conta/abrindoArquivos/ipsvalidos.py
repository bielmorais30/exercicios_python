def is_valid_ip_address(ip_address):
    octets = ip_address.split('.')
    if len(octets) != 4:
        return False
    for octet in octets:
        if not octet.isdigit() or int(octet) < 0 or int(octet) > 255:
            return False
    return True

valid_ips = []
invalid_ips = []

with open('ips.txt', 'r') as f:
    for line in f:
        ip_address = line.strip()
        if is_valid_ip_address(ip_address):
            valid_ips.append(ip_address)
        else:
            invalid_ips.append(ip_address)

with open('saida.txt', 'w') as f:
    f.write('[Endereços válidos:]\n')
    f.write('\n'.join(valid_ips))
    f.write('\n\n[Endereços inválidos:]\n')
    f.write('\n'.join(invalid_ips))