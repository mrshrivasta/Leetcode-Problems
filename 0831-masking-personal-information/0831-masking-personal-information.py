class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            s = s.lower()
            name, domain = s.split('@')
            return f"{name[0]}*****{name[-1]}@{domain}"
        else:
            digits = re.sub(r'\D', '', s)
            local = f"***-***-{digits[-4:]}"
            country_len = len(digits) - 10
            if country_len == 0:
                return local
            return f"+{'*' * country_len}-{local}"