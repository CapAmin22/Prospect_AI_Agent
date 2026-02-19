import smtplib
import socket
import dns.resolver
from typing import Tuple

def verify_email_smtp(email: str) -> Tuple[bool, float]:
    """
    Perform SMTP handshake to verify email existence.
    Catches timeouts and returns baseline score for safety.
    """
    domain = email.split('@')[-1]
    try:
        # Get MX record
        records = dns.resolver.resolve(domain, 'MX')
        mx_record = str(records[0].exchange)
        
        # Connect to SMTP server
        server = smtplib.SMTP(timeout=10)
        server.connect(mx_record)
        server.helo(server.local_hostname)
        server.mail('verify@prospect-agent.ai')
        code, message = server.rcpt(email)
        server.quit()
        
        if code == 250:
            return True, 90.0
        else:
            return False, 0.0
            
    except (socket.timeout, dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, ConnectionRefusedError):
        # Graceful failover to baseline score per PRD
        return False, 55.0
    except Exception:
        return False, 0.0
