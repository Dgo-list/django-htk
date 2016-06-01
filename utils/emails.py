import copy
import time

def email_permutator(domain, first_name='', middle_name='', last_name=''):
    from htk.constants.emails.permutations import EMAIL_PERMUTATION_PATTERNS
    domain = domain.lower()
    first_name = first_name.lower()
    middle_name = middle_name.lower()
    last_name = last_name.lower()
    parts = {
        'fn' : first_name,
        'fi' : first_name[0] if first_name else '',
        'mn' : middle_name,
        'mi' : middle_name[0] if middle_name else '',
        'ln' : last_name,
        'li' : last_name[0] if last_name else '',
        'domain' : domain,
    }

    email_possibilities = []
    email_patterns = copy.copy(EMAIL_PERMUTATION_PATTERNS)
    for email_pattern in email_patterns:
        base = email_pattern.replace('{', '%(').replace('}', ')s') + '@%(domain)s'
        email_possibility = base % parts
        email_possibilities.append(email_possibility)

    email_permutations = list(set(email_possibilities))
    return email_permutations

def find_company_email_for_name(domain, first_name='', middle_name='', last_name=''):
    from htk.lib.fullcontact.utils import find_person_by_email
    email_permutations = email_permutator(
        domain,
        first_name=first_name,
        middle_name=middle_name,
        last_name=last_name
    )
    the_email = None
    for email in email_permutations:
        person = find_person_by_email(email)
        if person:
            the_email = email
            break
        else:
            time.sleep(1)
    return the_email
