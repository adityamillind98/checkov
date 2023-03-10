from checkov.arm.checks.resource.NSGRulePortAccessRestricted import NSGRulePortAccessRestricted


class NSGRuleRDPAccessRestricted(NSGRulePortAccessRestricted):
    def __init__(self) -> None:
        super().__init__(
            name="Ensure that RDP access is restricted from the internet", check_id="CKV_AZURE_9", port=3389
        )


check = NSGRuleRDPAccessRestricted()
