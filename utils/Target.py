import ipaddress
from . import FileHandling
from . import TargetValidation


class Target:
    def __init__(self, target):
        self.target = target
        self.type = ''
        self.findings = []

    def add_finding(self, finding):
        self.findings.append(finding)

    @staticmethod
    def validate_targets(targets, output_path):
        valid_targets = []
        invalid_targets = []
        for tgt in targets:
            if TargetValidation.is_valid_ip_address(tgt):
                valid_targets.append(Target(tgt))
            elif TargetValidation.is_valid_network_block(tgt):
                network = ipaddress.ip_network(tgt, strict=False)
                for ip in network:
                    valid_targets.append(Target(ip))
            elif TargetValidation.is_valid_domain(tgt):
                valid_targets.append(Target(tgt))
            else:
                invalid_targets.append(tgt)
        if invalid_targets:
            FileHandling.write_invalid_targets(output_path, invalid_targets)
            print(f"Error: Invalid targets have been identified. Check the {output_path}"
                "and log files in the output directory.")
        if not valid_targets:
            print("No valid target or file path provided.")

        return valid_targets
    
        