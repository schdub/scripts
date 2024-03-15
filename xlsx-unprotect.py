import sys
import glob

def main():
    srcDir = './'
    if len(sys.argv) > 1:
        srcDir = sys.argv[1]
    if not srcDir.endswith('/'):
        srcDir = srcDir + '/'
    srcDir = srcDir + 'xl/worksheets/sheet*.xml'
    for sheetFilePath in glob.glob(srcDir):
        sheetFile = open(sheetFilePath, 'r')
        content = sheetFile.read()
        sheetFile.close()
        if len(content)==0:
            continue
        try:
            idx = content.index('<sheetProtection ')
            ide = content.index('/>', idx)
            protectValue = content[idx:ide+2]
            print(protectValue)

            sheetFile = open(sheetFilePath, 'w')
            sheetFile.write(content[:idx])
            sheetFile.write(content[ide+2:])
            sheetFile.close()
        except:
            pass

if __name__== "__main__":
    main()
