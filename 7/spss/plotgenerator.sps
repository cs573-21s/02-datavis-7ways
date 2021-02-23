* Encoding: UTF-8.
DATASET ACTIVATE DataSet1.
* Chart Builder.
GGRAPH
  /GRAPHDATASET NAME="graphdataset" VARIABLES=Weight MPG Manufacturer MISSING=LISTWISE 
    REPORTMISSING=NO
  /GRAPHSPEC SOURCE=INLINE
   INLINETEMPLATE="<setStyle type='scatter'><style size='20pt'/></setStyle>"
  /FITLINE TOTAL=NO SUBGROUP=NO
  /FRAME OUTER=NO INNER=NO
  /GRIDLINES XAXIS=YES YAXIS=YES
  /STYLE GRADIENT=NO.
BEGIN GPL
  SOURCE: s=userSource(id("graphdataset"))
  DATA: Weight=col(source(s), name("Weight"))
  DATA: MPG=col(source(s), name("MPG"))
  DATA: Manufacturer=col(source(s), name("Manufacturer"), unit.category())
  DATA: Weight1=col(source(s), name("Weight"))
  GUIDE: axis(dim(1), label("Weight"))
  GUIDE: axis(dim(2), label("MPG"))
  GUIDE: legend(aesthetic(aesthetic.color.interior), label("Manufacturer"))
  GUIDE: legend(aesthetic(aesthetic.size), label("Weight"))
  GUIDE: text.title(label("Scatter Plot of MPG by Weight by Manufacturer by Weight"))
  ELEMENT: point(position(Weight*MPG), color.interior(Manufacturer), size(Weight1),  transparency.exterior(transparency."0.5"), transparency.interior(transparency."0.5"))
END GPL.
