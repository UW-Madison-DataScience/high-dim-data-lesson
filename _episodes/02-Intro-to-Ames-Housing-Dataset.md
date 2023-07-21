---
title: The Ames housing dataset
teaching: 45
exercises: 2
keypoints:
objectives:
questions:
- "Here we introduce the data we'll be analyzing"
---
# Intro to Ames Housing Dataset

Here we introduce the data we'll be analyzing: The Ames Housing Dataset

## Load the dataset

Here we load the dataset from the sklearn library, and see a preview


```python
from sklearn.datasets import fetch_openml

# load the dataset
housing = fetch_openml(name="house_prices", as_frame=True)

df = housing.data.copy(deep=True) # create new DataFrame copy of original dataset
df = df.astype({'Id': int})        # set data type of Id to int
df = df.set_index('Id')           # set Id column to be the index of the DataFrame
df                                # evaluate result
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MSSubClass</th>
      <th>MSZoning</th>
      <th>LotFrontage</th>
      <th>LotArea</th>
      <th>Street</th>
      <th>Alley</th>
      <th>LotShape</th>
      <th>LandContour</th>
      <th>Utilities</th>
      <th>LotConfig</th>
      <th>...</th>
      <th>ScreenPorch</th>
      <th>PoolArea</th>
      <th>PoolQC</th>
      <th>Fence</th>
      <th>MiscFeature</th>
      <th>MiscVal</th>
      <th>MoSold</th>
      <th>YrSold</th>
      <th>SaleType</th>
      <th>SaleCondition</th>
    </tr>
    <tr>
      <th>Id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>60.0</td>
      <td>RL</td>
      <td>65.0</td>
      <td>8450.0</td>
      <td>Pave</td>
      <td>None</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>2008.0</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>2</th>
      <td>20.0</td>
      <td>RL</td>
      <td>80.0</td>
      <td>9600.0</td>
      <td>Pave</td>
      <td>None</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>FR2</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>2007.0</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>3</th>
      <td>60.0</td>
      <td>RL</td>
      <td>68.0</td>
      <td>11250.0</td>
      <td>Pave</td>
      <td>None</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>0.0</td>
      <td>9.0</td>
      <td>2008.0</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>4</th>
      <td>70.0</td>
      <td>RL</td>
      <td>60.0</td>
      <td>9550.0</td>
      <td>Pave</td>
      <td>None</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>2006.0</td>
      <td>WD</td>
      <td>Abnorml</td>
    </tr>
    <tr>
      <th>5</th>
      <td>60.0</td>
      <td>RL</td>
      <td>84.0</td>
      <td>14260.0</td>
      <td>Pave</td>
      <td>None</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>FR2</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>0.0</td>
      <td>12.0</td>
      <td>2008.0</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1456</th>
      <td>60.0</td>
      <td>RL</td>
      <td>62.0</td>
      <td>7917.0</td>
      <td>Pave</td>
      <td>None</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>0.0</td>
      <td>8.0</td>
      <td>2007.0</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>1457</th>
      <td>20.0</td>
      <td>RL</td>
      <td>85.0</td>
      <td>13175.0</td>
      <td>Pave</td>
      <td>None</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>None</td>
      <td>MnPrv</td>
      <td>None</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>2010.0</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>1458</th>
      <td>70.0</td>
      <td>RL</td>
      <td>66.0</td>
      <td>9042.0</td>
      <td>Pave</td>
      <td>None</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>None</td>
      <td>GdPrv</td>
      <td>Shed</td>
      <td>2500.0</td>
      <td>5.0</td>
      <td>2010.0</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>1459</th>
      <td>20.0</td>
      <td>RL</td>
      <td>68.0</td>
      <td>9717.0</td>
      <td>Pave</td>
      <td>None</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>0.0</td>
      <td>4.0</td>
      <td>2010.0</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>1460</th>
      <td>20.0</td>
      <td>RL</td>
      <td>75.0</td>
      <td>9937.0</td>
      <td>Pave</td>
      <td>None</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>0.0</td>
      <td>6.0</td>
      <td>2008.0</td>
      <td>WD</td>
      <td>Normal</td>
    </tr>
  </tbody>
</table>
<p>1460 rows × 79 columns</p>
</div>




```python
print(df.columns.tolist())
```

    ['MSSubClass', 'MSZoning', 'LotFrontage', 'LotArea', 'Street', 'Alley', 'LotShape', 'LandContour', 'Utilities', 'LotConfig', 'LandSlope', 'Neighborhood', 'Condition1', 'Condition2', 'BldgType', 'HouseStyle', 'OverallQual', 'OverallCond', 'YearBuilt', 'YearRemodAdd', 'RoofStyle', 'RoofMatl', 'Exterior1st', 'Exterior2nd', 'MasVnrType', 'MasVnrArea', 'ExterQual', 'ExterCond', 'Foundation', 'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinSF1', 'BsmtFinType2', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', 'Heating', 'HeatingQC', 'CentralAir', 'Electrical', '1stFlrSF', '2ndFlrSF', 'LowQualFinSF', 'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath', 'BedroomAbvGr', 'KitchenAbvGr', 'KitchenQual', 'TotRmsAbvGrd', 'Functional', 'Fireplaces', 'FireplaceQu', 'GarageType', 'GarageYrBlt', 'GarageFinish', 'GarageCars', 'GarageArea', 'GarageQual', 'GarageCond', 'PavedDrive', 'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'PoolQC', 'Fence', 'MiscFeature', 'MiscVal', 'MoSold', 'YrSold', 'SaleType', 'SaleCondition']


## Dataset Preview Exercises

> ## How many features are there?
> > ## Solution
> >
> > 79
> > ##### EXERCISE_END
> > 
> > #### EXERCISE: How many observations are there?
> > ##### ANSWER: 1460
> > ##### EXERCISE_END
> > #### EXERCISE: What are all the feature names?
> > ##### ANSWER:
> > ~~~
> > print(df.columns.tolist())
> > ~~~
> > {: .language-python}
> > ~~~
> > ['MSSubClass', 'MSZoning', 'LotFrontage', 'LotArea', 'Street', 'Alley', 'LotShape', 'LandContour', 'Utilities', 'LotConfig', 'LandSlope', 'Neighborhood', 'Condition1', 'Condition2', 'BldgType', 'HouseStyle', 'OverallQual', 'OverallCond', 'YearBuilt', 'YearRemodAdd', 'RoofStyle', 'RoofMatl', 'Exterior1st', 'Exterior2nd', 'MasVnrType', 'MasVnrArea', 'ExterQual', 'ExterCond', 'Foundation', 'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinSF1', 'BsmtFinType2', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', 'Heating', 'HeatingQC', 'CentralAir', 'Electrical', '1stFlrSF', '2ndFlrSF', 'LowQualFinSF', 'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath', 'BedroomAbvGr', 'KitchenAbvGr', 'KitchenQual', 'TotRmsAbvGrd', 'Functional', 'Fireplaces', 'FireplaceQu', 'GarageType', 'GarageYrBlt', 'GarageFinish', 'GarageCars', 'GarageArea', 'GarageQual', 'GarageCond', 'PavedDrive', 'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'PoolQC', 'Fence', 'MiscFeature', 'MiscVal', 'MoSold', 'YrSold', 'SaleType', 'SaleCondition']
> > ~~~
> > {: .output}
> > ##### EXERCISE_END
> > 
> > # How do I find out what these features mean?
> > ## Read the Data Dictionary
> > 
> > 
> > ```python
> > from IPython.display import display, Pretty
> > 
> > # the housing object we created in step one above contains a Data Dictionary for the Dataset
> > display(Pretty(housing.DESCR))
> > ```
> > 
> > 
> > Ask a home buyer to describe their dream house, and they probably won't begin with the height of the basement ceiling or the proximity to an east-west railroad. But this playground competition's dataset proves that much more influences price negotiations than the number of bedrooms or a white-picket fence.
> > 
> > With 79 explanatory variables describing (almost) every aspect of residential homes in Ames, Iowa, this competition challenges you to predict the final price of each home.
> > 
> > MSSubClass: Identifies the type of dwelling involved in the sale.
> > 
> > 20	1-STORY 1946 & NEWER ALL STYLES
> > 30	1-STORY 1945 & OLDER
> > 40	1-STORY W/FINISHED ATTIC ALL AGES
> > 45	1-1/2 STORY - UNFINISHED ALL AGES
> > 50	1-1/2 STORY FINISHED ALL AGES
> > 60	2-STORY 1946 & NEWER
> > 70	2-STORY 1945 & OLDER
> > 75	2-1/2 STORY ALL AGES
> > 80	SPLIT OR MULTI-LEVEL
> > 85	SPLIT FOYER
> > 90	DUPLEX - ALL STYLES AND AGES
> > 120	1-STORY PUD (Planned Unit Development) - 1946 & NEWER
> > 150	1-1/2 STORY PUD - ALL AGES
> > 160	2-STORY PUD - 1946 & NEWER
> > 180	PUD - MULTILEVEL - INCL SPLIT LEV/FOYER
> > 190	2 FAMILY CONVERSION - ALL STYLES AND AGES
> > 
> > MSZoning: Identifies the general zoning classification of the sale.
> > 
> > A	Agriculture
> > C	Commercial
> > FV	Floating Village Residential
> > I	Industrial
> > RH	Residential High Density
> > RL	Residential Low Density
> > RP	Residential Low Density Park
> > RM	Residential Medium Density
> > 
> > LotFrontage: Linear feet of street connected to property
> > 
> > LotArea: Lot size in square feet
> > 
> > Street: Type of road access to property
> > 
> > Grvl	Gravel
> > Pave	Paved
> > 
> > Alley: Type of alley access to property
> > 
> > Grvl	Gravel
> > Pave	Paved
> > NA 	No alley access
> > 
> > LotShape: General shape of property
> > 
> > Reg	Regular
> > IR1	Slightly irregular
> > IR2	Moderately Irregular
> > IR3	Irregular
> > 
> > LandContour: Flatness of the property
> > 
> > Lvl	Near Flat/Level
> > Bnk	Banked - Quick and significant rise from street grade to building
> > HLS	Hillside - Significant slope from side to side
> > Low	Depression
> > 
> > Utilities: Type of utilities available
> > 
> > AllPub	All public Utilities (E,G,W,& S)
> > NoSewr	Electricity, Gas, and Water (Septic Tank)
> > NoSeWa	Electricity and Gas Only
> > ELO	Electricity only
> > 
> > LotConfig: Lot configuration
> > 
> > Inside	Inside lot
> > Corner	Corner lot
> > CulDSac	Cul-de-sac
> > FR2	Frontage on 2 sides of property
> > FR3	Frontage on 3 sides of property
> > 
> > LandSlope: Slope of property
> > 
> > Gtl	Gentle slope
> > Mod	Moderate Slope
> > Sev	Severe Slope
> > 
> > Neighborhood: Physical locations within Ames city limits
> > 
> > Blmngtn	Bloomington Heights
> > Blueste	Bluestem
> > BrDale	Briardale
> > BrkSide	Brookside
> > ClearCr	Clear Creek
> > CollgCr	College Creek
> > Crawfor	Crawford
> > Edwards	Edwards
> > Gilbert	Gilbert
> > IDOTRR	Iowa DOT and Rail Road
> > MeadowV	Meadow Village
> > Mitchel	Mitchell
> > Names	North Ames
> > NoRidge	Northridge
> > NPkVill	Northpark Villa
> > NridgHt	Northridge Heights
> > NWAmes	Northwest Ames
> > OldTown	Old Town
> > SWISU	South & West of Iowa State University
> > Sawyer	Sawyer
> > SawyerW	Sawyer West
> > Somerst	Somerset
> > StoneBr	Stone Brook
> > Timber	Timberland
> > Veenker	Veenker
> > 
> > Condition1: Proximity to various conditions
> > 
> > Artery	Adjacent to arterial street
> > Feedr	Adjacent to feeder street
> > Norm	Normal
> > RRNn	Within 200' of North-South Railroad
> > RRAn	Adjacent to North-South Railroad
> > PosN	Near positive off-site feature--park, greenbelt, etc.
> > PosA	Adjacent to postive off-site feature
> > RRNe	Within 200' of East-West Railroad
> > RRAe	Adjacent to East-West Railroad
> > 
> > Condition2: Proximity to various conditions (if more than one is present)
> > 
> > Artery	Adjacent to arterial street
> > Feedr	Adjacent to feeder street
> > Norm	Normal
> > RRNn	Within 200' of North-South Railroad
> > RRAn	Adjacent to North-South Railroad
> > PosN	Near positive off-site feature--park, greenbelt, etc.
> > PosA	Adjacent to postive off-site feature
> > RRNe	Within 200' of East-West Railroad
> > RRAe	Adjacent to East-West Railroad
> > 
> > BldgType: Type of dwelling
> > 
> > 1Fam	Single-family Detached
> > 2FmCon	Two-family Conversion; originally built as one-family dwelling
> > Duplx	Duplex
> > TwnhsE	Townhouse End Unit
> > TwnhsI	Townhouse Inside Unit
> > 
> > HouseStyle: Style of dwelling
> > 
> > 1Story	One story
> > 1.5Fin	One and one-half story: 2nd level finished
> > 1.5Unf	One and one-half story: 2nd level unfinished
> > 2Story	Two story
> > 2.5Fin	Two and one-half story: 2nd level finished
> > 2.5Unf	Two and one-half story: 2nd level unfinished
> > SFoyer	Split Foyer
> > SLvl	Split Level
> > 
> > OverallQual: Rates the overall material and finish of the house
> > 
> > 10	Very Excellent
> > 9	Excellent
> > 8	Very Good
> > 7	Good
> > 6	Above Average
> > 5	Average
> > 4	Below Average
> > 3	Fair
> > 2	Poor
> > 1	Very Poor
> > 
> > OverallCond: Rates the overall condition of the house
> > 
> > 10	Very Excellent
> > 9	Excellent
> > 8	Very Good
> > 7	Good
> > 6	Above Average
> > 5	Average
> > 4	Below Average
> > 3	Fair
> > 2	Poor
> > 1	Very Poor
> > 
> > YearBuilt: Original construction date
> > 
> > YearRemodAdd: Remodel date (same as construction date if no remodeling or additions)
> > 
> > RoofStyle: Type of roof
> > 
> > Flat	Flat
> > Gable	Gable
> > Gambrel	Gabrel (Barn)
> > Hip	Hip
> > Mansard	Mansard
> > Shed	Shed
> > 
> > RoofMatl: Roof material
> > 
> > ClyTile	Clay or Tile
> > CompShg	Standard (Composite) Shingle
> > Membran	Membrane
> > Metal	Metal
> > Roll	Roll
> > Tar&Grv	Gravel & Tar
> > WdShake	Wood Shakes
> > WdShngl	Wood Shingles
> > 
> > Exterior1st: Exterior covering on house
> > 
> > AsbShng	Asbestos Shingles
> > AsphShn	Asphalt Shingles
> > BrkComm	Brick Common
> > BrkFace	Brick Face
> > CBlock	Cinder Block
> > CemntBd	Cement Board
> > HdBoard	Hard Board
> > ImStucc	Imitation Stucco
> > MetalSd	Metal Siding
> > Other	Other
> > Plywood	Plywood
> > PreCast	PreCast
> > Stone	Stone
> > Stucco	Stucco
> > VinylSd	Vinyl Siding
> > Wd Sdng	Wood Siding
> > WdShing	Wood Shingles
> > 
> > Exterior2nd: Exterior covering on house (if more than one material)
> > 
> > AsbShng	Asbestos Shingles
> > AsphShn	Asphalt Shingles
> > BrkComm	Brick Common
> > BrkFace	Brick Face
> > CBlock	Cinder Block
> > CemntBd	Cement Board
> > HdBoard	Hard Board
> > ImStucc	Imitation Stucco
> > MetalSd	Metal Siding
> > Other	Other
> > Plywood	Plywood
> > PreCast	PreCast
> > Stone	Stone
> > Stucco	Stucco
> > VinylSd	Vinyl Siding
> > Wd Sdng	Wood Siding
> > WdShing	Wood Shingles
> > 
> > MasVnrType: Masonry veneer type
> > 
> > BrkCmn	Brick Common
> > BrkFace	Brick Face
> > CBlock	Cinder Block
> > None	None
> > Stone	Stone
> > 
> > MasVnrArea: Masonry veneer area in square feet
> > 
> > ExterQual: Evaluates the quality of the material on the exterior
> > 
> > Ex	Excellent
> > Gd	Good
> > TA	Average/Typical
> > Fa	Fair
> > Po	Poor
> > 
> > ExterCond: Evaluates the present condition of the material on the exterior
> > 
> > Ex	Excellent
> > Gd	Good
> > TA	Average/Typical
> > Fa	Fair
> > Po	Poor
> > 
> > Foundation: Type of foundation
> > 
> > BrkTil	Brick & Tile
> > CBlock	Cinder Block
> > PConc	Poured Contrete
> > Slab	Slab
> > Stone	Stone
> > Wood	Wood
> > 
> > BsmtQual: Evaluates the height of the basement
> > 
> > Ex	Excellent (100+ inches)
> > Gd	Good (90-99 inches)
> > TA	Typical (80-89 inches)
> > Fa	Fair (70-79 inches)
> > Po	Poor (<70 inches
> > NA	No Basement
> > 
> > BsmtCond: Evaluates the general condition of the basement
> > 
> > Ex	Excellent
> > Gd	Good
> > TA	Typical - slight dampness allowed
> > Fa	Fair - dampness or some cracking or settling
> > Po	Poor - Severe cracking, settling, or wetness
> > NA	No Basement
> > 
> > BsmtExposure: Refers to walkout or garden level walls
> > 
> > Gd	Good Exposure
> > Av	Average Exposure (split levels or foyers typically score average or above)
> > Mn	Mimimum Exposure
> > No	No Exposure
> > NA	No Basement
> > 
> > BsmtFinType1: Rating of basement finished area
> > 
> > GLQ	Good Living Quarters
> > ALQ	Average Living Quarters
> > BLQ	Below Average Living Quarters
> > Rec	Average Rec Room
> > LwQ	Low Quality
> > Unf	Unfinshed
> > NA	No Basement
> > 
> > BsmtFinSF1: Type 1 finished square feet
> > 
> > BsmtFinType2: Rating of basement finished area (if multiple types)
> > 
> > GLQ	Good Living Quarters
> > ALQ	Average Living Quarters
> > BLQ	Below Average Living Quarters
> > Rec	Average Rec Room
> > LwQ	Low Quality
> > Unf	Unfinshed
> > NA	No Basement
> > 
> > BsmtFinSF2: Type 2 finished square feet
> > 
> > BsmtUnfSF: Unfinished square feet of basement area
> > 
> > TotalBsmtSF: Total square feet of basement area
> > 
> > Heating: Type of heating
> > 
> > Floor	Floor Furnace
> > GasA	Gas forced warm air furnace
> > GasW	Gas hot water or steam heat
> > Grav	Gravity furnace
> > OthW	Hot water or steam heat other than gas
> > Wall	Wall furnace
> > 
> > HeatingQC: Heating quality and condition
> > 
> > Ex	Excellent
> > Gd	Good
> > TA	Average/Typical
> > Fa	Fair
> > Po	Poor
> > 
> > CentralAir: Central air conditioning
> > 
> > N	No
> > Y	Yes
> > 
> > Electrical: Electrical system
> > 
> > SBrkr	Standard Circuit Breakers & Romex
> > FuseA	Fuse Box over 60 AMP and all Romex wiring (Average)
> > FuseF	60 AMP Fuse Box and mostly Romex wiring (Fair)
> > FuseP	60 AMP Fuse Box and mostly knob & tube wiring (poor)
> > Mix	Mixed
> > 
> > 1stFlrSF: First Floor square feet
> > 
> > 2ndFlrSF: Second floor square feet
> > 
> > LowQualFinSF: Low quality finished square feet (all floors)
> > 
> > GrLivArea: Above grade (ground) living area square feet
> > 
> > BsmtFullBath: Basement full bathrooms
> > 
> > BsmtHalfBath: Basement half bathrooms
> > 
> > FullBath: Full bathrooms above grade
> > 
> > HalfBath: Half baths above grade
> > 
> > Bedroom: Bedrooms above grade (does NOT include basement bedrooms)
> > 
> > Kitchen: Kitchens above grade
> > 
> > KitchenQual: Kitchen quality
> > 
> > Ex	Excellent
> > Gd	Good
> > TA	Typical/Average
> > Fa	Fair
> > Po	Poor
> > 
> > TotRmsAbvGrd: Total rooms above grade (does not include bathrooms)
> > 
> > Functional: Home functionality (Assume typical unless deductions are warranted)
> > 
> > Typ	Typical Functionality
> > Min1	Minor Deductions 1
> > Min2	Minor Deductions 2
> > Mod	Moderate Deductions
> > Maj1	Major Deductions 1
> > Maj2	Major Deductions 2
> > Sev	Severely Damaged
> > Sal	Salvage only
> > 
> > Fireplaces: Number of fireplaces
> > 
> > FireplaceQu: Fireplace quality
> > 
> > Ex	Excellent - Exceptional Masonry Fireplace
> > Gd	Good - Masonry Fireplace in main level
> > TA	Average - Prefabricated Fireplace in main living area or Masonry Fireplace in basement
> > Fa	Fair - Prefabricated Fireplace in basement
> > Po	Poor - Ben Franklin Stove
> > NA	No Fireplace
> > 
> > GarageType: Garage location
> > 
> > 2Types	More than one type of garage
> > Attchd	Attached to home
> > Basment	Basement Garage
> > BuiltIn	Built-In (Garage part of house - typically has room above garage)
> > CarPort	Car Port
> > Detchd	Detached from home
> > NA	No Garage
> > 
> > GarageYrBlt: Year garage was built
> > 
> > GarageFinish: Interior finish of the garage
> > 
> > Fin	Finished
> > RFn	Rough Finished
> > Unf	Unfinished
> > NA	No Garage
> > 
> > GarageCars: Size of garage in car capacity
> > 
> > GarageArea: Size of garage in square feet
> > 
> > GarageQual: Garage quality
> > 
> > Ex	Excellent
> > Gd	Good
> > TA	Typical/Average
> > Fa	Fair
> > Po	Poor
> > NA	No Garage
> > 
> > GarageCond: Garage condition
> > 
> > Ex	Excellent
> > Gd	Good
> > TA	Typical/Average
> > Fa	Fair
> > Po	Poor
> > NA	No Garage
> > 
> > PavedDrive: Paved driveway
> > 
> > Y	Paved
> > P	Partial Pavement
> > N	Dirt/Gravel
> > 
> > WoodDeckSF: Wood deck area in square feet
> > 
> > OpenPorchSF: Open porch area in square feet
> > 
> > EnclosedPorch: Enclosed porch area in square feet
> > 
> > 3SsnPorch: Three season porch area in square feet
> > 
> > ScreenPorch: Screen porch area in square feet
> > 
> > PoolArea: Pool area in square feet
> > 
> > PoolQC: Pool quality
> > 
> > Ex	Excellent
> > Gd	Good
> > TA	Average/Typical
> > Fa	Fair
> > NA	No Pool
> > 
> > Fence: Fence quality
> > 
> > GdPrv	Good Privacy
> > MnPrv	Minimum Privacy
> > GdWo	Good Wood
> > MnWw	Minimum Wood/Wire
> > NA	No Fence
> > 
> > MiscFeature: Miscellaneous feature not covered in other categories
> > 
> > Elev	Elevator
> > Gar2	2nd Garage (if not described in garage section)
> > Othr	Other
> > Shed	Shed (over 100 SF)
> > TenC	Tennis Court
> > NA	None
> > 
> > MiscVal: $Value of miscellaneous feature
> > 
> > MoSold: Month Sold (MM)
> > 
> > YrSold: Year Sold (YYYY)
> > 
> > SaleType: Type of sale
> > 
> > WD 	Warranty Deed - Conventional
> > CWD	Warranty Deed - Cash
> > VWD	Warranty Deed - VA Loan
> > New	Home just constructed and sold
> > COD	Court Officer Deed/Estate
> > Con	Contract 15% Down payment regular terms
> > ConLw	Contract Low Down payment and low interest
> > ConLI	Contract Low Interest
> > ConLD	Contract Low Down
> > Oth	Other
> > 
> > SaleCondition: Condition of sale
> > 
> > Normal	Normal Sale
> > Abnorml	Abnormal Sale -  trade, foreclosure, short sale
> > AdjLand	Adjoining Land Purchase
> > Alloca	Allocation - two linked properties with separate deeds, typically condo with a garage unit
> > Family	Sale between family members
> > Partial	Home was not completed when last assessed (associated with New Homes)
> > 
> > Downloaded from openml.org.
> > 
> > 
> > ## Feature Exercises
> > 
> > #### EXERCISE_START
> > What information is represented by BsmtFinType2?
> > ## Solution
> >
> > Rating of basement finished area (if multiple types)
> {:.solution}
{:.challenge}

#### EXERCISE_START
What type of variable is BsmtFinType2 (categorical or numeric, then nominal/ordinal or discrete/continuous)?
> > ## Solution
> >
> > categorical, ordinate
> {:.solution}
{:.challenge}

#### EXERCISE_START
What information is represented by GrLivArea?
> > ## Solution
> >
> > Above grade (ground) living area square feet
> {:.solution}
{:.challenge}

#### EXERCISE_START
What type of variable is GrLivArea? (categorical or numeric, then nominal/ordinal or discrete/continuous)?
> > ## Solution
> >
> > numeric, discrete
> {:.solution}
{:.challenge}




# Load the Target Variable - Housing Price


```python
import pandas as pd

housing_price_df = pd.DataFrame(housing.target) # load data into dataframe
housing_price_df.describe()                     # create numeric summary of that data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SalePrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>1460.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>180921.195890</td>
    </tr>
    <tr>
      <th>std</th>
      <td>79442.502883</td>
    </tr>
    <tr>
      <th>min</th>
      <td>34900.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>129975.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>163000.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>214000.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>755000.000000</td>
    </tr>
  </tbody>
</table>
</div>



## Price Exercises

#### EXERCISE_START
What is the range of housing prices in the dataset?
> > ## Solution
> >
> > min: $34,900, max: $755,000
> {:.solution}
{:.challenge}

#### EXERCISE_START
Are the price data skewed? What distribution might you expect?
> > ## Solution
> >
> > yes, positive/right handed skew. Expect positive/right handed skew from a long tail to outlier high values
> {:.solution}
{:.challenge}


# Plot housing price values


```python
import helper_functions
helper_functions.plot_salesprice(
    housing_price_df,
    # ylog=True
)
```







# Summary

In this session we:
1. Introduced the Ames Housing Dataset
2. Determined the number of features and observations
3. Understood some variables
4. Viewed the 'target variable': SalePrice


```python

```