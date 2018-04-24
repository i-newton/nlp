import sys
import re

pat_sub = [(r".*(Hello|Hi)\s([A-z]+).*", r"Hi stranger"),
           (r".*How are you\s*(doing)?.*", r"i am fine, and you?"),
           (r".*I ('m|am) (ok|doing well).*", r"i am glad to hear you are \2")]


def get_eliza_response(statement):
    response = None
    for p_s in pat_sub:
        pat, sub = p_s
        p = re.compile(pat)
        response = p.sub(sub, statement)
        if response != statement:
            return response
        else:
            response = None

    if response is None:
        return "Sorry i do not understand you," \
               "please re-formulate the statement"


def main(argv):
    if len(argv)<=1:
        raise Exception("Need 2 or more arguments")
    statement = argv[1]
    response = get_eliza_response(statement)
    print(response)


if __name__ == "__main__":
    main(sys.argv)

