import sys
from subprocess import check_output
from sampa2x import getPhoneticStrings


def phonetize(s):
    ipa = check_output(["espeak", "-q", "--ipa",  '-v', 'de', s]).decode('utf-8')
    return ipa


if __name__ == "__main__":
  german = sys.argv[1].strip()
  phonetic = phonetize(german)
  sampa = getPhoneticStrings(False, ipa=phonetic)
  print(german)
  print("phonetic (IPA): " + phonetic)
  print(sampa)