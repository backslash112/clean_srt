#!/usr/bin/env python

def clean_srt(file_name):
    with open () as fin:
        for line in fin:
            print(line[0])
            print(line[0].isalpha())
            if line[0].isalpha():
                new_result += line
    return new_result.replace('\n', ' ')

def save(txt):
    file = open("ted_new.txt", "w")
    file.write(txt)
    file.close()


def run():
    file_name = "ted.srt"
    txt = clean_srt(file_name)
    save(txt)

if __name__ == "__main__":
    run()
