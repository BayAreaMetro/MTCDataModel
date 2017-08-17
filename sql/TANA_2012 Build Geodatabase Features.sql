-- Build Tom Tom Geo Database Features

-- Build Network Features/Tables

SELECT * INTO  [Network].dbo.NW FROM [TANA_2012].tana.NW
SELECT * INTO  [Network].dbo.JC FROM [TANA_2012].tana.JC
SELECT * INTO  [Network].dbo.SG FROM [TANA_2012].dbo.SG
SELECT * INTO  [Network].dbo.MN FROM [TANA_2012].tana.MN
SELECT * INTO  [Network].dbo.TS FROM [TANA_2012].tana.TS
SELECT * INTO  [Network].dbo.CF FROM [TANA_2012].tana.CF
SELECT * INTO  [Network].dbo.RR FROM [TANA_2012].dbo.RR
SELECT * INTO  [Network].dbo.LN FROM [TANA_2012].tana.LN

--Network Tables

SELECT * INTO  [Network].dbo.SP FROM [TANA_2012_Tables].dbo.SP
SELECT * INTO  [Network].dbo.SI FROM [TANA_2012_Tables].dbo.SI
SELECT * INTO  [Network].dbo.RS FROM [TANA_2012_Tables].dbo.RS
SELECT * INTO  [Network].dbo.TD FROM [TANA_2012_Tables].dbo.TD
SELECT * INTO  [Network].dbo.TC FROM [TANA_2012_Tables].dbo.TC
SELECT * INTO  [Network].dbo.TL FROM [TANA_2012_Tables].dbo.TL
SELECT * INTO  [Network].dbo.TP FROM [TANA_2012_Tables].dbo.TP
SELECT * INTO  [Network].dbo.TG FROM [TANA_2012_Tables].dbo.TG
SELECT * INTO  [Network].dbo.RD FROM [TANA_2012_Tables].dbo.RD
SELECT * INTO  [Network].dbo.IG FROM [TANA_2012_Tables].dbo.IG
SELECT * INTO  [Network].dbo.MN_2R FROM [TANA_2012_Tables].dbo.MN_2R
SELECT * INTO  [Network].dbo.MN_IS FROM [TANA_2012_Tables].dbo.IS_
SELECT * INTO  [Network].dbo.ST FROM [TANA_2012_Tables].dbo.ST
SELECT * INTO  [Network].dbo.TT FROM [TANA_2012_Tables].dbo.TT
SELECT * INTO  [Network].dbo.PC FROM [TANA_2012_Tables].dbo.PC
SELECT * INTO  [Network].dbo.PCNM FROM [TANA_2012_Tables].dbo.PCNM
SELECT * INTO  [Network].dbo.RN FROM [TANA_2012_Tables].dbo.RN
SELECT * INTO  [Network].dbo.MN_TO FROM [TANA_2012_Tables].dbo.TO_
SELECT * INTO  [Network].dbo.RFNM FROM [TANA_2012_Tables].dbo.RFNM
SELECT * INTO  [Network].dbo.NWEA FROM [TANA_2012_Tables].dbo.NWEA
SELECT * INTO  [Network].dbo.PE FROM [TANA_2012_Tables].dbo.PE
SELECT * INTO  [Network].dbo.SE FROM [TANA_2012_Tables].dbo.SE
Select * INTO [Network].dbo.AXAS FROM [TANA_2012_Tables].dbo.AXAS
Select * INTO [Network].dbo.AXAV FROM [TANA_2012_Tables].dbo.AXAV

-- Lane Information Tables

SELECT * INTO  [Network].dbo.LL FROM [TANA_2012_Tables].dbo.LL
SELECT * INTO  [Network].dbo.LD FROM [TANA_2012_Tables].dbo.LD
SELECT * INTO  [Network].dbo.LI FROM [TANA_2012_Tables].dbo.LI
SELECT * INTO  [Network].dbo.LT FROM [TANA_2012_Tables].dbo.LT
SELECT * INTO  [Network].dbo.LF FROM [TANA_2012_Tables].dbo.LF
SELECT * INTO  [Network].dbo.SL FROM [TANA_2012_Tables].dbo.SL
SELECT * INTO  [Network].dbo.LP FROM [TANA_2012_Tables].dbo.LP
SELECT * INTO  [Network].dbo.PM FROM [TANA_2012_Tables].dbo.PM
SELECT * INTO  [Network].dbo.LE FROM [TANA_2012_Tables].dbo.LE



--Build Geocode Database Features/Tables

--Features

SELECT * INTO  [Geocode].dbo.GC FROM [TANA_2012].tana.GC
SELECT * INTO  [Geocode].dbo.AA FROM [TANA_2012].dbo.AA
SELECT * INTO  [Geocode].dbo.AP FROM [TANA_2012].dbo.AP
SELECT * INTO  [Geocode].dbo.PD FROM [TANA_2012].dbo.PD
SELECT * INTO  [Geocode].dbo.A8 FROM [TANA_2012].dbo.A8
SELECT * INTO  [Geocode].dbo.BU FROM [TANA_2012].tana.BU

-- Tables

SELECT * INTO  [Geocode].dbo.PC FROM [TANA_2012_Tables].dbo.PC
SELECT * INTO  [Geocode].dbo.IH FROM [TANA_2012_Tables].dbo.IH
SELECT * INTO  [Geocode].dbo.SC FROM [TANA_2012_Tables].dbo.SC
SELECT * INTO  [Geocode].dbo.AB FROM [TANA_2012_Tables].dbo.AB
SELECT * INTO  [Geocode].dbo.TA FROM [TANA_2012_Tables].dbo.TA
SELECT * INTO  [Geocode].dbo.EP FROM [TANA_2012_Tables].dbo.EP
SELECT * INTO  [Geocode].dbo.NP FROM [TANA_2012_Tables].dbo.NP
SELECT * INTO  [Geocode].dbo.PCNM FROM [TANA_2012_Tables].dbo.PCNM

-- Build Basemap Database Features/Tables

-- Features

Select * INTO [Basemap].dbo.PD FROM [TANA_2012].dbo.PD
Select * INTO [Basemap].dbo.AP FROM [TANA_2012].dbo.AP
Select * INTO [Basemap].dbo.OA01 FROM [TANA_2012].dbo.OA01
Select * INTO [Basemap].dbo.OA02 FROM [TANA_2012].dbo.OA02
Select * INTO [Basemap].dbo.OA03 FROM [TANA_2012].dbo.OA03
Select * INTO [Basemap].dbo.OA04 FROM [TANA_2012].dbo.OA04
Select * INTO [Basemap].dbo.OA05 FROM [TANA_2012].dbo.OA05
Select * INTO [Basemap].dbo.OA06 FROM [TANA_2012].dbo.OA06
Select * INTO [Basemap].dbo.OA07 FROM [TANA_2012].dbo.OA07
Select * INTO [Basemap].dbo.OA08 FROM [TANA_2012].dbo.OA08
Select * INTO [Basemap].dbo.OA09 FROM [TANA_2012].dbo.OA09
Select * INTO [Basemap].dbo.OA10 FROM [TANA_2012].dbo.OA10
Select * INTO [Basemap].dbo.OA11 FROM [TANA_2012].dbo.OA11
Select * INTO [Basemap].dbo.SM FROM [TANA_2012].dbo.POI_SM
Select * INTO [Basemap].dbo.BU FROM [TANA_2012].tana.BU
Select * INTO [Basemap].dbo.BL FROM [TANA_2012].tana.BL

-- Administrative Areas

Select * INTO [Basemap].dbo.A0 FROM [TANA_2012].dbo.A0
Select * INTO [Basemap].dbo.A1 FROM [TANA_2012].dbo.A1
Select * INTO [Basemap].dbo.A2 FROM [TANA_2012].dbo.A2
Select * INTO [Basemap].dbo.A3 FROM [TANA_2012].dbo.A3
Select * INTO [Basemap].dbo.A4 FROM [TANA_2012].dbo.A4
Select * INTO [Basemap].dbo.A5 FROM [TANA_2012].dbo.A5
Select * INTO [Basemap].dbo.A6 FROM [TANA_2012].dbo.A6
Select * INTO [Basemap].dbo.A7 FROM [TANA_2012].dbo.A7
Select * INTO [Basemap].dbo.A8 FROM [TANA_2012].dbo.A8
Select * INTO [Basemap].dbo.A9 FROM [TANA_2012].dbo.A9
Select * INTO [Basemap].dbo.SG FROM [TANA_2012].dbo.SG
Select * INTO [Basemap].dbo.POI_PI FROM [TANA_2012].dbo.POI_PI
Select * INTO [Basemap].dbo.AA FROM [TANA_2012].dbo.AA


-- Railroads

Select * INTO [Basemap].dbo.RR FROM [TANA_2012].dbo.RR

-- Streets and Ferries

Select * INTO [Basemap].dbo.Streets_00 FROM [TANA_2012].tana.Streets_00
Select * INTO [Basemap].dbo.Streets_01 FROM [TANA_2012].tana.Streets_01
Select * INTO [Basemap].dbo.Streets_02 FROM [TANA_2012].tana.Streets_02
Select * INTO [Basemap].dbo.Streets_03 FROM [TANA_2012].tana.STREETS_03
Select * INTO [Basemap].dbo.Streets_04 FROM [TANA_2012].tana.STREETS_04
Select * INTO [Basemap].dbo.Streets_05 FROM [TANA_2012].tana.STREETS_05
Select * INTO [Basemap].dbo.Streets_06 FROM [TANA_2012].tana.STREETS_06
Select * INTO [Basemap].dbo.Streets_07 FROM [TANA_2012].tana.STREETS_07
Select * INTO [Basemap].dbo.Streets_08 FROM [TANA_2012].tana.STREETS_08
Select * INTO [Basemap].dbo.FE FROM [TANA_2012].tana.FE

-- Water Areas and Lines

Select * INTO [Basemap].dbo.WL FROM [TANA_2012].dbo.WL
Select * INTO [Basemap].dbo.WA FROM [TANA_2012].dbo.WA

-- Land Use and Land Cover

Select * INTO [Basemap].dbo.LU FROM [TANA_2012].tana.LU
Select * INTO [Basemap].dbo.LC FROM [TANA_2012].tana.LC

Select * INTO [Basemap].dbo.PS FROM [TANA_2012].dbo.PS
Select * INTO [Basemap].dbo.MN_AS FROM [TANA_2012].dbo.AS_
Select * INTO [Basemap].dbo.LS FROM [TANA_2012].tana.LS

--Tables

Select * INTO [Basemap].dbo.PDNM FROM [TANA_2012_Tables].dbo.PDNM
Select * INTO [Basemap].dbo.PDEA FROM [TANA_2012_Tables].dbo.PDEA
Select * INTO [Basemap].dbo.OANM FROM [TANA_2012_Tables].dbo.OANM
Select * INTO [Basemap].dbo.OAEA FROM [TANA_2012_Tables].dbo.OAEA
Select * INTO [Basemap].dbo.BN FROM [TANA_2012_Tables].dbo.BN
Select * INTO [Basemap].dbo.BE FROM [TANA_2012_Tables].dbo.BE
Select * INTO [Basemap].dbo.BA FROM [TANA_2012_Tables].dbo.BA
Select * INTO [Basemap].dbo.AXAS FROM [TANA_2012_Tables].dbo.AXAS
Select * INTO [Basemap].dbo.AXAV FROM [TANA_2012_Tables].dbo.AXAV
Select * INTO [Basemap].dbo.TA FROM [TANA_2012_Tables].dbo.TA
Select * INTO [Basemap].dbo.SA FROM [TANA_2012_Tables].dbo.SA
Select * INTO [Basemap].dbo.PP FROM [TANA_2012_Tables].dbo.PP
Select * INTO [Basemap].dbo.SE FROM [TANA_2012_Tables].dbo.SE
Select * INTO [Basemap].dbo.OL FROM [TANA_2012_Tables].dbo.OL
Select * INTO [Basemap].dbo.AE FROM [TANA_2012_Tables].dbo.AE
Select * INTO [Basemap].dbo.AD FROM [TANA_2012_Tables].dbo.AD
Select * INTO [Basemap].dbo.AI FROM [TANA_2012_Tables].dbo.AI
Select * INTO [Basemap].dbo.VR FROM [TANA_2012_Tables].dbo.VR
Select * INTO [Basemap].dbo.POI_PIAS FROM [TANA_2012_Tables].dbo.POI_PIAS
Select * INTO [Basemap].dbo.POI_PIAV FROM [TANA_2012_Tables].dbo.POI_PIAV
Select * INTO [Basemap].dbo.AANM FROM [TANA_2012_Tables].dbo.AANM
Select * INTO [Basemap].dbo.AAEA FROM [TANA_2012_Tables].dbo.AAEA
Select * INTO [Basemap].dbo.AB FROM [TANA_2012_Tables].dbo.AB
Select * INTO [Basemap].dbo.RRNM FROM [TANA_2012_Tables].dbo.RRNM
Select * INTO [Basemap].dbo.RREA FROM [TANA_2012_Tables].dbo.RREA
Select * INTO [Basemap].dbo.WXEA FROM [TANA_2012_Tables].dbo.WXEA
Select * INTO [Basemap].dbo.WXNM FROM [TANA_2012_Tables].dbo.WXNM
Select * INTO [Basemap].dbo.LXEA FROM [TANA_2012_Tables].dbo.LXEA
Select * INTO [Basemap].dbo.LXNM FROM [TANA_2012_Tables].dbo.LXNM
Select * INTO [Basemap].dbo.SXEA FROM [TANA_2012_Tables].dbo.SXEA
Select * INTO [Basemap].dbo.SXNM FROM [TANA_2012_Tables].dbo.SXNM
Select * INTO [Basemap].dbo.NP FROM [TANA_2012_Tables].dbo.NP
Select * INTO [Basemap].dbo.EP FROM [TANA_2012_Tables].dbo.EP

-- Points of Interest Features/Tables

-- Features
Select * INTO [POI].dbo.POI_PI FROM [TANA_2012].dbo.POI_PI
Select * INTO [POI].dbo.POI_SM FROM [TANA_2012].dbo.POI_SM


-- Tables

Select * INTO [POI].dbo.PIAS FROM [TANA_2012_Tables].dbo.POI_PIAS
Select * INTO [POI].dbo.PIAV FROM [TANA_2012_Tables].dbo.POI_PIAV
Select * INTO [POI].dbo.PIEA FROM [TANA_2012_Tables].dbo.PIEA
Select * INTO [POI].dbo.PE FROM [TANA_2012_Tables].dbo.PE
Select * INTO [POI].dbo.PR FROM [TANA_2012_Tables].dbo.PR
Select * INTO [POI].dbo.VR FROM [TANA_2012_Tables].dbo.VR
Select * INTO [POI].dbo.PINM FROM [TANA_2012_Tables].dbo.PINM
Select * INTO [POI].dbo.SMNM FROM [TANA_2012_Tables].dbo.SMNM
Select * INTO [POI].dbo.SMEA FROM [TANA_2012_Tables].dbo.SMEA
Select * INTO [POI].dbo.SA FROM [TANA_2012_Tables].dbo.SA


-- Other Named Areas Features/Tables

Select * INTO [OtherNameAreas].dbo.PDEA FROM [TANA_2012_Tables].dbo.PDEA
Select * INTO [OtherNameAreas].dbo.PDNM FROM [TANA_2012_Tables].dbo.PDNM
Select * INTO [OtherNameAreas].dbo.PD FROM [TANA_2012].dbo.PD
Select * INTO [OtherNameAreas].dbo.SM FROM [TANA_2012].dbo.POI_SM
Select * INTO [OtherNameAreas].dbo.BN FROM [TANA_2012_Tables].dbo.BN
Select * INTO [OtherNameAreas].dbo.BE FROM [TANA_2012_Tables].dbo.BE
Select * INTO [OtherNameAreas].dbo.BA FROM [TANA_2012_Tables].dbo.BA
Select * INTO [OtherNameAreas].dbo.OANM FROM [TANA_2012_Tables].dbo.OANM
Select * INTO [OtherNameAreas].dbo.OAEA FROM [TANA_2012_Tables].dbo.OAEA
Select * INTO [OtherNameAreas].dbo.TA FROM [TANA_2012_Tables].dbo.TA
Select * INTO [OtherNameAreas].dbo.BU FROM [TANA_2012].tana.BU
Select * INTO [OtherNameAreas].dbo.OA01 FROM [TANA_2012].dbo.OA01
Select * INTO [OtherNameAreas].dbo.OA02 FROM [TANA_2012].dbo.OA02
Select * INTO [OtherNameAreas].dbo.OA03 FROM [TANA_2012].dbo.OA03
Select * INTO [OtherNameAreas].dbo.OA04 FROM [TANA_2012].dbo.OA04
Select * INTO [OtherNameAreas].dbo.OA05 FROM [TANA_2012].dbo.OA05
Select * INTO [OtherNameAreas].dbo.OA06 FROM [TANA_2012].dbo.OA06
Select * INTO [OtherNameAreas].dbo.OA07 FROM [TANA_2012].dbo.OA07
Select * INTO [OtherNameAreas].dbo.OA08 FROM [TANA_2012].dbo.OA08
Select * INTO [OtherNameAreas].dbo.OA09 FROM [TANA_2012].dbo.OA09
Select * INTO [OtherNameAreas].dbo.OA10 FROM [TANA_2012].dbo.OA10
Select * INTO [OtherNameAreas].dbo.OA11 FROM [TANA_2012].dbo.OA11
