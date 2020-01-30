def crack_pass(passwords, attempt):
    if attempt in passwords:
        return [ attempt ]
    passlens = map(len, passwords)
    minlen,maxlen = min(passlens), max(passlens)
    if len(attempt) <= minlen: return False

    for i in range(minlen, min(len(attempt), maxlen)+1):
        fw = attempt[:i]
        if fw in passwords:
            restpass = list(passwords)
            restpass.remove(fw)
            ret = crack_pass(restpass, attempt[i:])
            if ret:
                return [ fw ] + ret
    return False
