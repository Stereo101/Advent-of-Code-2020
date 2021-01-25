from advent import Session
import re

aoc = Session(2020,4)
with aoc.fp() as fp:
    L = [line.strip() for line in fp.readlines()]

def valid_height(v):
    if("in" in v):
        n = v.split("in")[0]
        return (59 <= int(n) <= 76)
    elif("cm" in v):
        n = v.split("cm")[0]
        return (150 <= int(n) <= 193)
    return False

req_fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
valid_rules = {
    "byr":lambda x: len(x) == 4 and (1920<=int(x)<=2002),
    "iyr":lambda x: len(x) == 4 and (2010<=int(x)<=2020),
    "eyr":lambda x: len(x) == 4 and (2020<=int(x)<=2030),
    "hgt":valid_height,
    "hcl":lambda x: re.match(r"^#[0-9a-f]{6}$",x) is not None,
    "ecl":lambda x: x in ["amb","blu","brn","gry","grn","hzl","oth"],
    "pid":lambda x: re.match(r"^[0-9]{9}$",x) is not None,
    "cid":lambda x: True
}
def valid_field(k, v):
    if(k in valid_rules):
        return valid_rules[k](v)
    s = f"unknown field '{k}'"
    raise Exception(s)
        
def passport_itr(L):
    passport = {}
    for line in L:
        if(line == "" or line == "\n"):
            yield passport
            passport = {}
            continue
        for pair in line.split(" "):
            k,v = pair.split(":")
            passport[k] = v
    if(len(passport) > 0):
        yield passport
    return

def passport_is_valid(passport):
    return  passport_has_req_fields(passport) and \
            all(valid_field(field,passport[field]) for field in req_fields)

def passport_has_req_fields(passport):
    return all(field in passport for field in req_fields)

full_passports = [p for p in passport_itr(L) if passport_has_req_fields(p)]
valid_passports = [p for p in full_passports if passport_is_valid(p)]
print("silver:",len(full_passports))
print("gold:",len(valid_passports))
