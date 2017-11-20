import hashlib


class MacUtils:
    @staticmethod
    def build_mac(*args):
        sb = ""
        for arg in args:
            sb += str(arg)
        sb = sb.encode('UTF-8')
        mac = hashlib.sha256(sb).hexdigest()
        return mac