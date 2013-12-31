#!/usr/bin/python

import struct, os, sys

class F51:
    fieldwidths = (1, 4, 10, 1, 1, 2, 30, 4, 2, 3, 11, 11, 11, 11, 1, 1, 1, 1, 5, 5,
            5, 5, 1, 1, 1, 1, 2, 2, 3, 3, 5, 5, 5, 5, 5, 5, 6, 6, 4, 4, 10, 9, 10, 9)
    fieldnames = ("RecType", "Version", "TLID", "SIDE1", "Source", "FEDIRP", "FENAME", "FETYPE", "FEDIRS",
            "CFCC", "FRADDL", "TOADDL", "FRADDR", "TOADDR", "FRIADDL", "TOIADDL", "FRIADDR", "TOIADDR",
            "ZIPL", "ZIPR", "AIANHHFPL", "AINHHFPR", "AIHHTLIL", "AIHHTLIR", "Census1", "Census2",
            "StateL", "StateR", "CountyL", "CountyR", "COUSUBL", "COUSUBR", "SUBMCDL", "SUBMCDR",
            "PlaceL", "PlaceR", "TractL", "TractR", "BlockL", "BlockR", "FrLong", "FrLat", "ToLong", "ToLat")
    rtype = "1"


    def __init__ (self, tgrfile):
        self.data = []
        if not os.access(tgrfile + ".F5"+self.rtype, os.R_OK):
           self.f = ""
           return;
        self.f = open(tgrfile + ".F5"+self.rtype, 'r')
        self.tgrf = tgrfile
        self.fmtstring = ''.join('%ds' % f for f in self.fieldwidths)
        self.parse = struct.Struct(self.fmtstring).unpack_from
#        print "starting f51"

    def readall(self, fp):
        fldnams = [self.fieldnames[0], self.fieldnames[2] ]
        fldnams.extend(self.fieldnames[4:13])
        fldnams.extend(self.fieldnames[26:39])
        fldnams.append("wkt")
        fp.write('"' + '","'.join(fldnams) + '"' + "\n")

        if ( self.f == "" ):
            return

#        print ":" + self.tgrf 
        line = self.f.readline();
        wkt=""
        vtxs=0
        f52 = F52(self.tgrf)

        while (line):
           fields = self.parse(line)
           if ( fields[0] == '1' ):
               tlid = fields[2]
#               print "tlid: " + tlid
               wkt = "linestring("+ str(float(fields[40])/1000000.0) + " " +  str(float(fields[41])/1000000.0)
               wkt = wkt + f52.readTLID(tlid) 
               wkt = wkt +  str(float(fields[42])/1000000.0) + " " +  str(float(fields[43])/1000000.0) + ")"
#               print  'fields:', fields, wkt
               flds = [fields[0], fields[2]]
               flds.extend(fields[4:13])
               flds.extend(fields[26:39])
               flds.append(wkt)
               fld2=[]
               for l in flds:
                  fld2.append(l.strip())
               fp.write('"' + '","'.join(fld2) + '"' + "\n")
 
           line = self.f.readline()

        self.f.close


class F52:
    fieldwidths = (1, 4, 10, 3, 
            10, 9, 10, 9, 10, 9, 10, 9, 10, 9,
            10, 9, 10, 9, 10, 9, 10, 9, 10, 9)
    fieldnames = ("RecType", "Version", "TLID", "RTSEQ", 
            "Long1", "Lat1", "Long1", "Lat2", "Long3", "Lat3", "Long4", "Lat4", "Long5", "Lat5",
            "Long6", "Lat6", "Long7", "Lat7", "Long8", "Lat8", "Long9", "Lat9", "Long10", "Lat10" )
    rtype = "2"
    skipped = 0

    def __init__ (self, tgrfile):
        self.data = []
        if not os.access(tgrfile + ".F5"+self.rtype, os.R_OK):
           self.f = ""
           return;
        self.f = open(tgrfile + ".F5"+self.rtype, 'r')

        self.fmtstring = ''.join('%ds' % f for f in self.fieldwidths)
        self.parse = struct.Struct(self.fmtstring).unpack_from
        self.tlid=""
        print "starting f52"

    def readTLID (self, rTLID):

        print "f52: entering when tlid " + self.tlid + " while looking for " + rTLID
        
        if ( rTLID == "" ):
          return ","
        if ( rTLID > self.tlid ):  # looking forward
            self.line = self.f.readline();

        wkt = ","
        vlist = []
        if ( not self.line ):
          return ","
        fields = self.parse(self.line)
        self.tlid = fields[2]

        print "starting additional scan with vlist = ", vlist
        while (self.line and rTLID >= self.tlid):

           if ( fields[0] == '2' ):  # its a record type 2
               if ( rTLID != self.tlid ):
                  self.skipped = self.skipped + 1
                  print "skipping: " + self.tlid
               else:
                  print "reading " + self.tlid
                  print "   " + self.line
                  vlist.append([fields[3],fields[4:len(fields)]])  # add RTSQ and new vertices to list 

           self.line = self.f.readline()
           if ( self.line ):  # handle the last line in file nicely
               fields = self.parse(self.line)
               self.tlid = fields[2]

        vlist.sort()  # sort the vertex cards 
        print "Note: ", rTLID, vlist, len(vlist)

        for vc in range(len(vlist)):
           print "pulling card ", vc, vlist[vc]
           for vtx in range(10):
               vp = vlist[vc][1][(vtx*2):(vtx*2)+2]
               if ( vp[0] != "+000000000" ):
                   print "pulling vertex ", vtx, vlist[vc][1][(vtx*2):(vtx*2)+2]
                   wkt = wkt + str(float(vp[0])/1000000.0) + " " +  str(float(vp[1])/1000000.0) + ","
            
        print "f52: exiting when tlid " + self.tlid + " while looking for " + rTLID + " with " + wkt
        
        return wkt


class F5I:  # TIGER to Poly Links
    fieldwidths = (1, 4, 10, 5, 1, 5, 10, 5, 10, 1)
    fieldnames = ("RecType", "Version", "TLID", "File", "RTLink", 
            "CenIdL", "PolyIdL", "CenIdR", "PolyIdR", "Filler")
    rtype = "I"
    pad_buf = ""
    
    def __init__ (self, tgrfile):
        self.data = []
        if not os.access(tgrfile + ".F5"+self.rtype, os.R_OK):
           self.f = ""
           return;
        self.f = open(tgrfile + ".F5"+self.rtype, 'r')

        self.fmtstring = ''.join('%ds' % f for f in self.fieldwidths)
        self.parse = struct.Struct(self.fmtstring).unpack_from
        self.pad_buf = "                       "
        self.tlid=""
#        print "starting f5I"

    def readall(self, fp):
        fldnams = self.fieldnames
        fp.write('"' + '","'.join(fldnams) + '"' + "\n")

        if ( self.f == "" ):
            return

#        print ":" + self.tgrf 
        line = self.f.readline();

        while (line):
           fields = self.parse(line + self.pad_buf)
           if ( fields[0] == self.rtype ):
               tlid = fields[2]
               flds = fields
               fld2=[]
               for l in flds:
                  fld2.append(l.strip())
               fp.write('"' + '","'.join(fld2) + '"' + "\n")
 
           line = self.f.readline()

        return ""

class F54:   # TLID link to Altnames
    fieldwidths = (1, 4, 10, 3, 8, 8, 8, 8, 8)
    fieldnames = ("RecType", "Version", "TLID", "RTSeq", 
            "AltFeatId1", "AltFeatId2", "AltFeatId3", "AltFeatId4", "AltFeatId5")
    rtype = "4"

    def __init__ (self, tgrfile):
        self.data = []
        if not os.access(tgrfile + ".F5"+self.rtype, os.R_OK):
           self.f = ""
           return;
        self.f = open(tgrfile + ".F5"+self.rtype, 'r')

        self.fmtstring = ''.join('%ds' % f for f in self.fieldwidths)
        self.parse = struct.Struct(self.fmtstring).unpack_from
        self.tlid=""
#        print "starting f54"

    def readall(self, fp):
        fldnams = self.fieldnames
        fp.write('"' + '","'.join(fldnams) + '"' + "\n")

        if ( self.f == "" ):
            return

#        print ":" + self.tgrf 
        line = self.f.readline();

        while (line):
           fields = self.parse(line)
           if ( fields[0] == '4' ):
               tlid = fields[2]
               flds = fields
               fld2=[]
               for l in flds:
                  fld2.append(l.strip())
               fp.write('"' + '","'.join(fld2) + '"' + "\n")
 
           line = self.f.readline()

        return ""

class F55:   # Feature Names
    fieldwidths = (1, 5, 8, 2, 30, 4, 2)
    fieldnames = ("RecType", "File", "FeatId", "FeDirP", "FeName", "FeType", "FeDirS") 
    rtype = "5"

    def __init__ (self, tgrfile):
        self.data = []
        if not os.access(tgrfile + ".F5"+self.rtype, os.R_OK):
           self.f = ""
           return;
        self.f = open(tgrfile + ".F5"+self.rtype, 'r')
        self.fmtstring = ''.join('%ds' % f for f in self.fieldwidths)
        self.parse = struct.Struct(self.fmtstring).unpack_from
        self.tlid=""
#        print "starting f55"

    def readall(self, fp):
        fldnams = self.fieldnames
        fp.write('"' + '","'.join(fldnams) + '"' + "\n")

        if ( self.f == "" ):
            return

#        print ":" + self.tgrf 
        line = self.f.readline();

        while (line):
           fields = self.parse(line)
           if ( fields[0] == self.rtype ):
               tlid = fields[2]
               flds = fields
               fld2=[]
               for l in flds:
                  fld2.append(l.strip())
               fp.write('"' + '","'.join(fld2) + '"' +"\n")
 
           line = self.f.readline()

        return ""

class F56:   # Additional data for TLID
    fieldwidths = (1, 4, 10, 3, 11, 11, 11, 11, 1, 1, 1, 1, 5, 5)
    fieldnames = ("RecType", "Version", "TLID", "RTSQ", 
        "FrAddL", "ToAddL", "FrAddR", "ToAddR", "FrIAddL", "ToIAddL", "FrIAddR", "ToIAddR",
        "ZIPL", "ZIPR") 
    rtype = "6"   

    def __init__ (self, tgrfile):
        self.data = []
        if not os.access(tgrfile + ".F5"+self.rtype, os.R_OK):
           self.f = ""
           return;
        self.f = open(tgrfile + ".F5"+self.rtype, 'r')

        self.fmtstring = ''.join('%ds' % f for f in self.fieldwidths)
        self.parse = struct.Struct(self.fmtstring).unpack_from
        self.tlid=""
#        print "starting f56"

    def readall(self, fp):
        fldnams = self.fieldnames
        fp.write('"' + '","'.join(fldnams) + '"' + "\n")

        if ( self.f == "" ):
            return

#        print ":" + self.tgrf 
        line = self.f.readline();

        while (line):
           fields = self.parse(line)
           if ( fields[0] == self.rtype ):
               tlid = fields[2]
               flds = fields
               fld2=[]
               for l in flds:
                  fld2.append(l.strip())
               fp.write('"' + '","'.join(fld2) + '"' + "\n")
 
           line = self.f.readline()

        return ""


class F5A:   # Polygon Attribute data
    fieldwidths = (1, 4, 2, 3, 5, 10, 5, 5, 5, 6, 4, 2, 4, 3, 1, 2, 2, 5, 5, 5, 5, 6, 4, 1)
    fieldnames = ("RecType", "Version", "State", "County", "CenId", 
        "PolyId", "AIANAFP", "CouSub", "Place", "Tract", "CTBNA_Basic", "CTBNA_Sufx", 
        "Block", "Block_Basic", "Block_Sufx", "CD101", "CD103", "ESCode", "MSCode",
        "SSCode", "USCode", "TAZ", "UA", "UR")
    rtype = "A"

    def __init__ (self, tgrfile):
        self.data = []
        if not os.access(tgrfile + ".F5"+self.rtype, os.R_OK):
           self.f = ""
           return;
        self.f = open(tgrfile + ".F5"+self.rtype, 'r')

        self.fmtstring = ''.join('%ds' % f for f in self.fieldwidths)
        self.parse = struct.Struct(self.fmtstring).unpack_from
        self.tlid=""
#        print "starting f5P"

    def readall(self, fp):
        fldnams = self.fieldnames
        fp.write('"' + '","'.join(fldnams) + '"' + "\n")

        if ( self.f == "" ):
            return

#        print ":" + self.tgrf 
        line = self.f.readline();

        while (line):
           fields = self.parse(line)
           if ( fields[0] == self.rtype ):
               tlid = fields[2]
               flds=[]
               flds.extend(fields)
             
               fld2=[]
               for l in flds:
                  fld2.append(l.strip())
               fp.write('"' + '","'.join(fld2) + '"' + "\n")
 
           line = self.f.readline()

        return ""


class F5P:   # Polygon data
    fieldwidths = (1, 4, 2, 3, 5, 10, 10, 9)
    fieldnames = ("RecType", "Version", "State", "County", "CenId", 
        "PolyId", "Long", "Lat", "WKT")
    rtype = "P"

    def __init__ (self, tgrfile):
        self.data = []
        if not os.access(tgrfile + ".F5"+self.rtype, os.R_OK):
           self.f = ""
           return;
        self.f = open(tgrfile + ".F5"+self.rtype, 'r')

        self.fmtstring = ''.join('%ds' % f for f in self.fieldwidths)
        self.parse = struct.Struct(self.fmtstring).unpack_from
        self.tlid=""
#        print "starting f5P"

    def readall(self, fp):
        fldnams = self.fieldnames
        fp.write('"' + '","'.join(fldnams) + '"' + "\n")

        if ( self.f == "" ):
            return

#        print ":" + self.tgrfile
        line = self.f.readline();

        while (line):
           fields = self.parse(line)
           if ( fields[0] == self.rtype ):
               tlid = fields[2]
               flds=[]
               flds.extend(fields[0:6])
               flds.append(str(float(fields[6])/1000000.0))
               flds.append(str(float(fields[7])/1000000.0))
             
               fld2=[]
               for l in flds:
                  fld2.append(l.strip())
               fld2.append('Point(' + flds[6] + ' ' + flds[7] + ')')
               fp.write('"' + '","'.join(fld2) + '"' + "\n")
 
           line = self.f.readline()

        return ""

class F57:   # Landmark data
    fieldwidths = (1, 4, 2, 3, 10, 1, 3, 30, 10, 9)
    fieldnames = ("RecType", "Version", "State", "County", "LandmarkId", 
        "Source", "CFCC", "LandmarkName", "Long", "Lat", "WKT")
    rtype = "7"
    pad_buf = ""

    def __init__ (self, tgrfile):
        self.data = []
        if not os.access(tgrfile + ".F5"+self.rtype, os.R_OK):
           self.f = ""
           return;
        self.f = open(tgrfile + ".F5"+self.rtype, 'r')

        self.fmtstring = ''.join('%ds' % f for f in self.fieldwidths)
        self.parse = struct.Struct(self.fmtstring).unpack_from
        self.need_size = struct.calcsize(self.fmtstring)
        self.pad_buf = "                           "

        self.tlid=""
#        print "starting f5" + self.rtype

    def readall(self, fp):
        fldnams = self.fieldnames
        fp.write('"' + '","'.join(fldnams) + '"' + "\n")

        if ( self.f == "" ):
            return

#        print ":" + self.tgrfile
        line = self.f.readline();

        while (line):
           fields = self.parse(line + self.pad_buf)
           if ( fields[0] == self.rtype ):
               flds=[]
               flds.extend(fields[0:8])
#               print "F7: ", fields[8], fields[9], fields
               if ( fields[8] != "          " ):
                   flds.append(str(float(fields[8])/1000000.0))
                   flds.append(str(float(fields[9])/1000000.0))
               else:
                   flds.append("")
                   flds.append("")

               fld2=[]
               for l in flds:
                  fld2.append(l.strip())
               if ( flds[8] > '        ' ):
                   fld2.append('Point(' + flds[8] + ' ' + flds[9] + ')')
               else:
                   fld2.append("")
               fp.write('"' + '","'.join(fld2) + '"' + "\n")
 
           line = self.f.readline()

        return ""


class F58:   # Landmark Poly Links
    fieldwidths = (1, 4, 2, 3, 10, 1, 3, 30, 10, 9)
    fieldnames = ("RecType", "Version", "State", "County", "CenId", "PolyId", 
        "LandmarkId") 
    rtype = "8"

    def __init__ (self, tgrfile):
        self.data = []
        if not os.access(tgrfile + ".F5"+self.rtype, os.R_OK):
           self.f = ""
           return;
        self.f = open(tgrfile + ".F5"+self.rtype, 'r')

        self.fmtstring = ''.join('%ds' % f for f in self.fieldwidths)
        self.parse = struct.Struct(self.fmtstring).unpack_from
        self.tlid=""
#        print "starting f5" + self.rtype

    def readall(self, fp):
        fldnams = self.fieldnames
        fp.write('"' + '","'.join(fldnams) + '"' + "\n")

        if ( self.f == "" ):
            return

#        print ":" + self.tgrfile
        line = self.f.readline();

        while (line):
           fields = self.parse(line)
           if ( fields[0] == self.rtype ):
               flds=[]
               flds.extend(fields)

               fld2=[]
               for l in flds:
                  fld2.append(l.strip())
               fp.write('"' + '","'.join(fld2) + '"' + "\n")
 
           line = self.f.readline()

        return ""

class F5S:  # Poly Extra
    fieldwidths = (1, 4, 5, 5, 10, 1, 4, 4, 5, 4, 1, 2, 2, 3,
             5, 5, 5, 5, 6, 4, 1, 2, 3, 3, 5, 1, 6, 2, 3, 5, 1, 5, 1, 1)
    fieldnames = ("RecType", "Version", "File", "CenId", 
            "PolyId", "Water", "MSACMSA", "PMSA", "AIANHH", "AIANHHCE",
            "AIHHTLI", "RS6", "State", "County", "Concit", "CouSub",
            "SUBMCD", "Place", "Tract", "Block", "Census6", "CDCU",
            "SLDU", "SLDL", "UGA", "BLKGRP", "VTD" ,"StateCol", "CountyCol",
            "BlockCol", "BlkSufCol", "ZCTA5", "UR", "UR90")
    rtype = "S"
    
    def __init__ (self, tgrfile):
        self.data = []
        if not os.access(tgrfile + ".F5"+self.rtype, os.R_OK):
           self.f = ""
           return;
        self.f = open(tgrfile + ".F5"+self.rtype, 'r')

        self.fmtstring = ''.join('%ds' % f for f in self.fieldwidths)
        self.parse = struct.Struct(self.fmtstring).unpack_from
        self.tlid=""
#        print "starting f5S"

    def readall(self, fp):
        fldnams = self.fieldnames
        fp.write('"' + '","'.join(fldnams) + '"' + "\n")

        if ( self.f == "" ):
            return

#        print ":" + self.tgrf 
        line = self.f.readline();

        while (line):
           fields = self.parse(line)
           if ( fields[0] == self.rtype ):
               tlid = fields[2]
               flds = fields
               fld2=[]
               for l in flds:
                  fld2.append(l.strip())
               fp.write('"' + '","'.join(fld2) + '"' + "\n")
 
           line = self.f.readline()

        return ""

# Main 

print "Starting TIGER 1992 read for: ", sys.argv[1] 
tfil="TGR" + sys.argv[1]

fP=open("dat/Chain.csv", "w")
f51=F51("tmp/"+tfil)
f51.readall(fP)
fP.close

fP=open("dat/FeatnameLink.csv", "w")
f54=F54("tmp/"+tfil)
f54.readall(fP)
fP.close

fP=open("dat/Featname.csv", "w")
f55=F55("tmp/"+tfil)
f55.readall(fP)
fP.close

fP=open("dat/Addr.csv", "w")
f56=F56("tmp/"+tfil)
f56.readall(fP)
fP.close

fP=open("dat/Landmark.csv", "w")
f57=F57("tmp/"+tfil)
f57.readall(fP)
fP.close

fP=open("dat/PolyAttr.csv", "w")
f5A=F5A("tmp/"+tfil)
f5A.readall(fP)
fP.close

fP=open("dat/PolyLink.csv", "w")
f5i=F5I("tmp/"+tfil)
f5i.readall(fP)
fP.close

fP=open("dat/PolyPt.csv", "w")
f5p=F5P("tmp/"+tfil)
f5p.readall(fP)
fP.close

fP=open("dat/PolyExtra.csv", "w")
f5s=F5S("tmp/"+tfil)
f5s.readall(fP)
fP.close



