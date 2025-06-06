import re

TOKEN_TYPES = [
    ("COMMENT",      r"\$.*"),
    ("KEYWORD",      r"\b(useJAVA|PYTHONuse|UseCSHARP|Cplusplus)\b"),
    ("NUMBER",       r"\b\d+(\.\d+)?\b"),
    ("STRING",       r'"[^"]*"'),
    ("VAR",          r"\#[a-zA-Z_]\w*"),
    ("LBRACE",       r"\{"),
    ("RBRACE",       r"\}"),
    ("IDENTIFIER",   r"[a-zA-Z_]\w*"),
    ("WHITESPACE",   r"\s+"),
    ("UNKNOWN",      r"."),
]

token_regex = "|".join(f"(?P<{name}>{pattern})" for name, pattern in TOKEN_TYPES)

def lexer(code):
    tokens = []
    for match in re.finditer(token_regex, code):
        kind = match.lastgroup
        value = match.group()
        if kind == "WHITESPACE":
            continue
        tokens.append((kind, value))
    return tokens
