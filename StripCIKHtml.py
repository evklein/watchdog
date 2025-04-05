import io

html = '''<a href="browse-edgar?action=getcompany&amp;CIK=1348831">0001348831</a>   VANGUARD 2005 DRILLING &amp; DEVELOPMENT PROGRAM
<a href="browse-edgar?action=getcompany&amp;CIK=891190">0000891190</a>   VANGUARD ADMIRAL FUNDS
<a href="browse-edgar?action=getcompany&amp;CIK=891190">0000891190</a>   VANGUARD ADMIRAL FUNDS INC
<a href="browse-edgar?action=getcompany&amp;CIK=947529">0000947529</a>   VANGUARD ADVISERS INC
<a href="browse-edgar?action=getcompany&amp;CIK=947529">0000947529</a>   VANGUARD ADVISERS INC /ADV
<a href="browse-edgar?action=getcompany&amp;CIK=1000578">0001000578</a>   VANGUARD AIRLINES INC \DE\
<a href="browse-edgar?action=getcompany&amp;CIK=1258324">0001258324</a>   VANGUARD ANIMATION LLC
<a href="browse-edgar?action=getcompany&amp;CIK=836906">0000836906</a>   VANGUARD ASSET ALLOCATION FUND INC
<a href="browse-edgar?action=getcompany&amp;CIK=1680208">0001680208</a>   VANGUARD ASSET MANAGEMENT, LTD
<a href="browse-edgar?action=getcompany&amp;CIK=836724">0000836724</a>   VANGUARD ASSOCIATES III L P
<a href="browse-edgar?action=getcompany&amp;CIK=1054810">0001054810</a>   VANGUARD ATLANTIC LTD
<a href="browse-edgar?action=getcompany&amp;CIK=889519">0000889519</a>   VANGUARD BALANCED INDEX FUND
<a href="browse-edgar?action=getcompany&amp;CIK=889519">0000889519</a>   VANGUARD BALANCED INDEX FUND INC
<a href="browse-edgar?action=getcompany&amp;CIK=889519">0000889519</a>   VANGUARD BALANCED INDEX FUNDS
<a href="browse-edgar?action=getcompany&amp;CIK=1674731">0001674731</a>   VANGUARD BEACHWOOD APARTMENTS, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=794105">0000794105</a>   VANGUARD BOND INDEX FUND INC
<a href="browse-edgar?action=getcompany&amp;CIK=794105">0000794105</a>   VANGUARD BOND INDEX FUNDS
<a href="browse-edgar?action=getcompany&amp;CIK=783401">0000783401</a>   VANGUARD CALIFORNIA TAX FREE FUND
<a href="browse-edgar?action=getcompany&amp;CIK=783401">0000783401</a>   VANGUARD CALIFORNIA TAX FREE FUNDS
<a href="browse-edgar?action=getcompany&amp;CIK=783401">0000783401</a>   VANGUARD CALIFORNIA TAX-FREE FUNDS
<a href="browse-edgar?action=getcompany&amp;CIK=830288">0000830288</a>   VANGUARD CAPITAL    
<a href="browse-edgar?action=getcompany&amp;CIK=830288">0000830288</a>   VANGUARD CAPITAL /BD
<a href="browse-edgar?action=getcompany&amp;CIK=1730578">0001730578</a>   VANGUARD CAPITAL WEALTH ADVISORS
<a href="browse-edgar?action=getcompany&amp;CIK=1326170">0001326170</a>   VANGUARD CAPITAL, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1370828">0001370828</a>   VANGUARD CAR RENTAL GROUP INC.
<a href="browse-edgar?action=getcompany&amp;CIK=1273878">0001273878</a>   VANGUARD CASH MANAGEMENT TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=771178">0000771178</a>   VANGUARD CELLULAR SYSTEMS INC
<a href="browse-edgar?action=getcompany&amp;CIK=1532203">0001532203</a>   VANGUARD CHARLOTTE FUNDS
<a href="browse-edgar?action=getcompany&amp;CIK=752177">0000752177</a>   VANGUARD CHESTER FUNDS
<a href="browse-edgar?action=getcompany&amp;CIK=1284858">0001284858</a>   VANGUARD CHESTER FUNDS
<a href="browse-edgar?action=getcompany&amp;CIK=1273878">0001273878</a>   VANGUARD CMT FUNDS  
<a href="browse-edgar?action=getcompany&amp;CIK=791107">0000791107</a>   VANGUARD CONVERTIBLE SECURITIES FUND
<a href="browse-edgar?action=getcompany&amp;CIK=791107">0000791107</a>   VANGUARD CONVERTIBLE SECURITIES FUND INC
<a href="browse-edgar?action=getcompany&amp;CIK=1683428">0001683428</a>   VANGUARD DEALER SERVICES, L.L.C.
<a href="browse-edgar?action=getcompany&amp;CIK=1497649">0001497649</a>   VANGUARD ENERGY CORP
<a href="browse-edgar?action=getcompany&amp;CIK=1321511">0001321511</a>   VANGUARD ENERGY GROUP, INC.
<a href="browse-edgar?action=getcompany&amp;CIK=826473">0000826473</a>   VANGUARD EQUITY INCOME FUND INC
<a href="browse-edgar?action=getcompany&amp;CIK=1340295">0001340295</a>   VANGUARD EXPLORATION CORP
<a href="browse-edgar?action=getcompany&amp;CIK=34066">0000034066</a>   VANGUARD EXPLORER FUND
<a href="browse-edgar?action=getcompany&amp;CIK=34066">0000034066</a>   VANGUARD EXPLORER FUND INC
<a href="browse-edgar?action=getcompany&amp;CIK=1142637">0001142637</a>   VANGUARD EXTENDED STOCK MAKET INDEX FUND
<a href="browse-edgar?action=getcompany&amp;CIK=1841609">0001841609</a>   VANGUARD FARMS INTERNATIONAL INC
<a href="browse-edgar?action=getcompany&amp;CIK=826473">0000826473</a>   VANGUARD FENWAY FUNDS
<a href="browse-edgar?action=getcompany&amp;CIK=1130926">0001130926</a>   VANGUARD FENWAY FUNDS
<a href="browse-edgar?action=getcompany&amp;CIK=933478">0000933478</a>   VANGUARD FIDUCIARY TRUST CO
<a href="browse-edgar?action=getcompany&amp;CIK=1603857">0001603857</a>   VANGUARD FINANCIAL TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=106444">0000106444</a>   VANGUARD FIXED INCOME SECURITIES FUND INC
<a href="browse-edgar?action=getcompany&amp;CIK=106444">0000106444</a>   VANGUARD FIXED INCOME SECURITIES FUNDS
<a href="browse-edgar?action=getcompany&amp;CIK=888451">0000888451</a>   VANGUARD FLORIDA INSURED TAX FREE FUND
<a href="browse-edgar?action=getcompany&amp;CIK=1174321">0001174321</a>   VANGUARD FLORIDA TAX FREE FUNDS
<a href="browse-edgar?action=getcompany&amp;CIK=888451">0000888451</a>   VANGUARD FLORIDA TAX-FREE FUND
<a href="browse-edgar?action=getcompany&amp;CIK=888451">0000888451</a>   VANGUARD FLORIDA TAX-FREE FUNDS
<a href="browse-edgar?action=getcompany&amp;CIK=1811242">0001811242</a>   VANGUARD GLOBAL ADVISERS, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=2013071">0002013071</a>   VANGUARD GOLD CAPITAL INC
<a href="browse-edgar?action=getcompany&amp;CIK=1746119">0001746119</a>   VANGUARD GREEN INVESTMENT LTD
<a href="browse-edgar?action=getcompany&amp;CIK=102909">0000102909</a>   VANGUARD GROUP INC  
<a href="browse-edgar?action=getcompany&amp;CIK=735286">0000735286</a>   VANGUARD GROUP INC  
<a href="browse-edgar?action=getcompany&amp;CIK=735286">0000735286</a>   VANGUARD GROUP INC /TA
<a href="browse-edgar?action=getcompany&amp;CIK=1807289">0001807289</a>   VANGUARD HARBOURVEST 2020 PRIVATE EQUITY FEEDER FUND L.P.
<a href="browse-edgar?action=getcompany&amp;CIK=1807286">0001807286</a>   VANGUARD HARBOURVEST 2020 PRIVATE EQUITY FUND L.P.
<a href="browse-edgar?action=getcompany&amp;CIK=1871481">0001871481</a>   VANGUARD HARBOURVEST 2021 PRIVATE EQUITY FEEDER FUND L.P.
<a href="browse-edgar?action=getcompany&amp;CIK=1871477">0001871477</a>   VANGUARD HARBOURVEST 2021 PRIVATE EQUITY FUND L.P.
<a href="browse-edgar?action=getcompany&amp;CIK=2020059">0002020059</a>   VANGUARD HARBOURVEST 2021 PRIVATE EQUITY HOLDINGS LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1920881">0001920881</a>   VANGUARD HARBOURVEST 2022 PRIVATE EQUITY FEEDER FUND L.P.
<a href="browse-edgar?action=getcompany&amp;CIK=1920852">0001920852</a>   VANGUARD HARBOURVEST 2022 PRIVATE EQUITY FUND L.P.
<a href="browse-edgar?action=getcompany&amp;CIK=2020058">0002020058</a>   VANGUARD HARBOURVEST 2022 PRIVATE EQUITY HOLDINGS LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1958781">0001958781</a>   VANGUARD HARBOURVEST 2023 PRIVATE EQUITY FEEDER FUND L.P.
<a href="browse-edgar?action=getcompany&amp;CIK=1958768">0001958768</a>   VANGUARD HARBOURVEST 2023 PRIVATE EQUITY FUND L.P.
<a href="browse-edgar?action=getcompany&amp;CIK=2014811">0002014811</a>   VANGUARD HARBOURVEST 2024 PRIVATE EQUITY FEEDER FUND L.P.
<a href="browse-edgar?action=getcompany&amp;CIK=2014810">0002014810</a>   VANGUARD HARBOURVEST 2024 PRIVATE EQUITY FUND L.P.
<a href="browse-edgar?action=getcompany&amp;CIK=2049251">0002049251</a>   VANGUARD HARBOURVEST 2025 PRIVATE EQUITY FUND L.P.
<a href="browse-edgar?action=getcompany&amp;CIK=1161106">0001161106</a>   VANGUARD HEALTH FINANCIAL CO INC
<a href="browse-edgar?action=getcompany&amp;CIK=1161106">0001161106</a>   VANGUARD HEALTH FINANCIAL CO LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1307389">0001307389</a>   VANGUARD HEALTH HOLDING CO I, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1307411">0001307411</a>   VANGUARD HEALTH HOLDING CO II, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1161103">0001161103</a>   VANGUARD HEALTH MANAGEMENT INC
<a href="browse-edgar?action=getcompany&amp;CIK=1045829">0001045829</a>   VANGUARD HEALTH SYSTEMS INC
<a href="browse-edgar?action=getcompany&amp;CIK=2053841">0002053841</a>   VANGUARD HIGHGROWTH FUND LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1307399">0001307399</a>   VANGUARD HOLDING CO I, INC.
<a href="browse-edgar?action=getcompany&amp;CIK=1307400">0001307400</a>   VANGUARD HOLDING CO II, INC.
<a href="browse-edgar?action=getcompany&amp;CIK=1731565">0001731565</a>   VANGUARD HOLDING COMPANY, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1649293">0001649293</a>   VANGUARD HOLDING CORP.
<a href="browse-edgar?action=getcompany&amp;CIK=932471">0000932471</a>   VANGUARD HORIZON FUND INC
<a href="browse-edgar?action=getcompany&amp;CIK=932471">0000932471</a>   VANGUARD HORIZON FUNDS
<a href="browse-edgar?action=getcompany&amp;CIK=1380307">0001380307</a>   VANGUARD IMAGING PARTNERS LLC
<a href="browse-edgar?action=getcompany&amp;CIK=36405">0000036405</a>   VANGUARD INDEX FUNDS
<a href="browse-edgar?action=getcompany&amp;CIK=1114857">0001114857</a>   VANGUARD INDEX FUNDS
<a href="browse-edgar?action=getcompany&amp;CIK=36405">0000036405</a>   VANGUARD INDEX FUNDS/
<a href="browse-edgar?action=getcompany&amp;CIK=36405">0000036405</a>   VANGUARD INDEX TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=862084">0000862084</a>   VANGUARD INSTITUTIONAL INDEX FUND
<a href="browse-edgar?action=getcompany&amp;CIK=862084">0000862084</a>   VANGUARD INSTITUTIONAL INDEX FUNDS
<a href="browse-edgar?action=getcompany&amp;CIK=846591">0000846591</a>   VANGUARD INSTITUTIONAL PORTFOLIOS INC
<a href="browse-edgar?action=getcompany&amp;CIK=1104225">0001104225</a>   VANGUARD INSURANCE AGENCY INC
<a href="browse-edgar?action=getcompany&amp;CIK=857489">0000857489</a>   VANGUARD INTERNATIONAL EQUITY INDEX FUND INC
<a href="browse-edgar?action=getcompany&amp;CIK=857489">0000857489</a>   VANGUARD INTERNATIONAL EQUITY INDEX FUNDS
<a href="browse-edgar?action=getcompany&amp;CIK=1305589">0001305589</a>   VANGUARD INVESTMENT EUROPE SA
<a href="browse-edgar?action=getcompany&amp;CIK=1898388">0001898388</a>   VANGUARD INVESTMENT HOLDINGS ONE (CAYMAN) L.P.
<a href="browse-edgar?action=getcompany&amp;CIK=1599779">0001599779</a>   VANGUARD INVESTMENT SERIES PLC
<a href="browse-edgar?action=getcompany&amp;CIK=1550100">0001550100</a>   VANGUARD INVESTMENTS AUSTRALIA, LTD.
<a href="browse-edgar?action=getcompany&amp;CIK=1016735">0001016735</a>   VANGUARD IV L P
<a href="browse-edgar?action=getcompany&amp;CIK=1585064">0001585064</a>   FIDELITY &amp; GUARANTY LIFE
<a href="browse-edgar?action=getcompany&amp;CIK=1965862">0001965862</a>   FIDELITY &amp; GUARANTY LIFE BUSINESS SERVICES, INC.
<a href="browse-edgar?action=getcompany&amp;CIK=1965861">0001965861</a>   FIDELITY &amp; GUARANTY LIFE HOLDINGS, INC.
<a href="browse-edgar?action=getcompany&amp;CIK=854241">0000854241</a>   FIDELITY &amp; GUARANTY LIFE INSURANCE CO
<a href="browse-edgar?action=getcompany&amp;CIK=1271886">0001271886</a>   FIDELITY &amp; TRUST FINANCIAL CORP
<a href="browse-edgar?action=getcompany&amp;CIK=1628278">0001628278</a>   FIDELITY (CANADA) ASSET MANAGEMENT ULC
<a href="browse-edgar?action=getcompany&amp;CIK=1916762">0001916762</a>   FIDELITY 2022 PRIVATE EQUITY MULTI-STRATEGY FUND LP
<a href="browse-edgar?action=getcompany&amp;CIK=1916721">0001916721</a>   FIDELITY 2022 PRIVATE EQUITY MULTI-STRATEGY FUND LP - OFFSHORE
<a href="browse-edgar?action=getcompany&amp;CIK=880195">0000880195</a>   FIDELITY ABERDEEN STREET TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=927384">0000927384</a>   FIDELITY ADVISOR ANNUITY FUND
<a href="browse-edgar?action=getcompany&amp;CIK=930867">0000930867</a>   FIDELITY ADVISOR CHINA FUND INC
<a href="browse-edgar?action=getcompany&amp;CIK=917951">0000917951</a>   FIDELITY ADVISOR EMERGING ASIA FUND INC
<a href="browse-edgar?action=getcompany&amp;CIK=926431">0000926431</a>   FIDELITY ADVISOR KOREA FUND INC
<a href="browse-edgar?action=getcompany&amp;CIK=729218">0000729218</a>   FIDELITY ADVISOR SERIES 8
<a href="browse-edgar?action=getcompany&amp;CIK=722574">0000722574</a>   FIDELITY ADVISOR SERIES I
<a href="browse-edgar?action=getcompany&amp;CIK=795422">0000795422</a>   FIDELITY ADVISOR SERIES II
<a href="browse-edgar?action=getcompany&amp;CIK=702533">0000702533</a>   FIDELITY ADVISOR SERIES III
<a href="browse-edgar?action=getcompany&amp;CIK=719451">0000719451</a>   FIDELITY ADVISOR SERIES IV
<a href="browse-edgar?action=getcompany&amp;CIK=803013">0000803013</a>   FIDELITY ADVISOR SERIES V
<a href="browse-edgar?action=getcompany&amp;CIK=1168353">0001168353</a>   FIDELITY ADVISOR SERIES V
<a href="browse-edgar?action=getcompany&amp;CIK=720318">0000720318</a>   FIDELITY ADVISOR SERIES VI
<a href="browse-edgar?action=getcompany&amp;CIK=315700">0000315700</a>   FIDELITY ADVISOR SERIES VII
<a href="browse-edgar?action=getcompany&amp;CIK=729218">0000729218</a>   FIDELITY ADVISOR SERIES VIII
<a href="browse-edgar?action=getcompany&amp;CIK=1771548">0001771548</a>   FIDELITY AG, INC.   
<a href="browse-edgar?action=getcompany&amp;CIK=1012471">0001012471</a>   FIDELITY ASSET MANAGEMENT INC /BD
<a href="browse-edgar?action=getcompany&amp;CIK=1411057">0001411057</a>   FIDELITY AVIATION CORP
<a href="browse-edgar?action=getcompany&amp;CIK=769207">0000769207</a>   FIDELITY BANCORP INC
<a href="browse-edgar?action=getcompany&amp;CIK=912219">0000912219</a>   FIDELITY BANCORP INC /DE/
<a href="browse-edgar?action=getcompany&amp;CIK=1095145">0001095145</a>   FIDELITY BANCORP INC EMPLOYEE STOCK OWNERSHIP PLAN
<a href="browse-edgar?action=getcompany&amp;CIK=825953">0000825953</a>   FIDELITY BANCSHARES NC INC /DE/
<a href="browse-edgar?action=getcompany&amp;CIK=2020154">0002020154</a>   FIDELITY BANCSHARES, INC.
<a href="browse-edgar?action=getcompany&amp;CIK=940654">0000940654</a>   FIDELITY BANKERS LIFE INSURANCE CO TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=1028336">0001028336</a>   FIDELITY BANKSHARES INC
<a href="browse-edgar?action=getcompany&amp;CIK=1619768">0001619768</a>   FIDELITY BEACH STREET TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=311884">0000311884</a>   FIDELITY BEACON STREET TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=823535">0000823535</a>   FIDELITY BOSTON STREET TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=700859">0000700859</a>   FIDELITY BOYLSTON STREET TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=2058468">0002058468</a>   FIDELITY BRIDGE HOLDINGS II, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1807072">0001807072</a>   FIDELITY BRIDGE HOLDINGS, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=908500">0000908500</a>   FIDELITY BROKERAGE SERVICES INC
<a href="browse-edgar?action=getcompany&amp;CIK=278082">0000278082</a>   FIDELITY BROKERAGE SERVICES LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1681155">0001681155</a>   FIDELITY BROMFIELD STREET TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=1419454">0001419454</a>   FIDELITY BUSINESS SERVICES INDIA PRIVATE LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1419454">0001419454</a>   FIDELITY BUSINESS SERVICES INDIA PRIVATE LTD
<a href="browse-edgar?action=getcompany&amp;CIK=718891">0000718891</a>   FIDELITY CALIFORNIA MUNICIPAL TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=878662">0000878662</a>   FIDELITY CALIFORNIA MUNICIPAL TRUST II
<a href="browse-edgar?action=getcompany&amp;CIK=1325867">0001325867</a>   FIDELITY CAP IV LLC 
<a href="browse-edgar?action=getcompany&amp;CIK=1359543">0001359543</a>   FIDELITY CAP V, LLC 
<a href="browse-edgar?action=getcompany&amp;CIK=1111696">0001111696</a>   FIDELITY CAPITAL CONCEPTS LTD
<a href="browse-edgar?action=getcompany&amp;CIK=35318">0000035318</a>   FIDELITY CAPITAL FUND INC
<a href="browse-edgar?action=getcompany&amp;CIK=35319">0000035319</a>   FIDELITY CAPITAL INVESTMENT PLANS
<a href="browse-edgar?action=getcompany&amp;CIK=1464424">0001464424</a>   FIDELITY CAPITAL OPERATING LIMITED PARTNERSHIP
<a href="browse-edgar?action=getcompany&amp;CIK=275309">0000275309</a>   FIDELITY CAPITAL TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=1051178">0001051178</a>   FIDELITY CAPITAL TRUST I
<a href="browse-edgar?action=getcompany&amp;CIK=1401097">0001401097</a>   FIDELITY CENTRAL INVESTMENT PORTFOLIOS II LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1303459">0001303459</a>   FIDELITY CENTRAL INVESTMENT PORTFOLIOS LLC
<a href="browse-edgar?action=getcompany&amp;CIK=354046">0000354046</a>   FIDELITY CHARLES STREET TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=1952558">0001952558</a>   FIDELITY CHERRY STREET TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=1905320">0001905320</a>   FIDELITY CO         
<a href="browse-edgar?action=getcompany&amp;CIK=356173">0000356173</a>   FIDELITY COLCHESTER STREET TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=205323">0000205323</a>   FIDELITY COMMONWEALTH TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=1364923">0001364923</a>   FIDELITY COMMONWEALTH TRUST II
<a href="browse-edgar?action=getcompany&amp;CIK=819118">0000819118</a>   FIDELITY CONCORD STREET TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=23355">0000023355</a>   FIDELITY CONGRESS STREET FUND
<a href="browse-edgar?action=getcompany&amp;CIK=24238">0000024238</a>   FIDELITY CONTRAFUND 
<a href="browse-edgar?action=getcompany&amp;CIK=2025802">0002025802</a>   FIDELITY CONVERTIBLE ARBITRAGE FUND LP
<a href="browse-edgar?action=getcompany&amp;CIK=2026043">0002026043</a>   FIDELITY CONVERTIBLE ARBITRAGE FUND LP - OFFSHORE
<a href="browse-edgar?action=getcompany&amp;CIK=1953520">0001953520</a>   FIDELITY CORE REAL ESTATE FUND
<a href="browse-edgar?action=getcompany&amp;CIK=225323">0000225323</a>   FIDELITY COURT STREET TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=880709">0000880709</a>   FIDELITY COURT STREET TRUST II
<a href="browse-edgar?action=getcompany&amp;CIK=945908">0000945908</a>   FIDELITY COVINGTON TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=1994803">0001994803</a>   FIDELITY CREDIT OPPORTUNITIES FEEDER FUND II LP
<a href="browse-edgar?action=getcompany&amp;CIK=1994793">0001994793</a>   FIDELITY CREDIT OPPORTUNITIES FUND II LP
<a href="browse-edgar?action=getcompany&amp;CIK=1302683">0001302683</a>   FIDELITY CUSTODIAN SERVICES INC
<a href="browse-edgar?action=getcompany&amp;CIK=1098151">0001098151</a>   FIDELITY D &amp; D BANCORP INC
<a href="browse-edgar?action=getcompany&amp;CIK=1145895">0001145895</a>   FIDELITY D&amp;D BANCORP INC
<a href="browse-edgar?action=getcompany&amp;CIK=1039264">0001039264</a>   FIDELITY DEFINED TRUST SERIES 4
<a href="browse-edgar?action=getcompany&amp;CIK=948251">0000948251</a>   FIDELITY DEFINED TRUSTS
<a href="browse-edgar?action=getcompany&amp;CIK=1032110">0001032110</a>   FIDELITY DEFINED TRUSTS MUNICIPAL INCOME TRUSTS SERIES I
<a href="browse-edgar?action=getcompany&amp;CIK=947056">0000947056</a>   FIDELITY DEFINED TRUSTS SERIES 1
<a href="browse-edgar?action=getcompany&amp;CIK=1012679">0001012679</a>   FIDELITY DEFINED TRUSTS SERIES 2
<a href="browse-edgar?action=getcompany&amp;CIK=1027384">0001027384</a>   FIDELITY DEFINED TRUSTS SERIES 3
<a href="browse-edgar?action=getcompany&amp;CIK=1050110">0001050110</a>   FIDELITY DEFINED TRUSTS SERIES 5
<a href="browse-edgar?action=getcompany&amp;CIK=1061006">0001061006</a>   FIDELITY DEFINED TRUSTS SERIES F
<a href="browse-edgar?action=getcompany&amp;CIK=839515">0000839515</a>   FIDELITY DEPOSIT &amp; DISCOUNT BANK /TA
<a href="browse-edgar?action=getcompany&amp;CIK=35331">0000035331</a>   FIDELITY DESTINY PORTFOLIOS
<a href="browse-edgar?action=getcompany&amp;CIK=812574">0000812574</a>   FIDELITY DEUTSCHE MARK PERFORMANCE PORTFOLIO L P
<a href="browse-edgar?action=getcompany&amp;CIK=1190415">0001190415</a>   FIDELITY DEVELOPMENT GROUP
<a href="browse-edgar?action=getcompany&amp;CIK=35341">0000035341</a>   FIDELITY DEVONSHIRE TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=1899996">0001899996</a>   FIDELITY DIRECT LENDING FUND, LP
<a href="browse-edgar?action=getcompany&amp;CIK=1908412">0001908412</a>   FIDELITY DIRECT LENDING INSTITUTIONAL FUND, LP
<a href="browse-edgar?action=getcompany&amp;CIK=1809390">0001809390</a>   FIDELITY DISTRESSED OPPORTUNITIES FUND I, LP
<a href="browse-edgar?action=getcompany&amp;CIK=1956247">0001956247</a>   FIDELITY DISTRESSED OPPORTUNITIES MASTER FUND I, LP
<a href="browse-edgar?action=getcompany&amp;CIK=1809386">0001809386</a>   FIDELITY DISTRESSED OPPORTUNITIES OFFSHORE FUND I, LP
<a href="browse-edgar?action=getcompany&amp;CIK=783343">0000783343</a>   FIDELITY DISTRIBUTORS COMPANY LLC
<a href="browse-edgar?action=getcompany&amp;CIK=35336">0000035336</a>   FIDELITY DISTRIBUTORS CORP
<a href="browse-edgar?action=getcompany&amp;CIK=732882">0000732882</a>   FIDELITY DISTRIBUTORS CORP
<a href="browse-edgar?action=getcompany&amp;CIK=35336">0000035336</a>   FIDELITY DISTRIBUTORS CORPORATION
<a href="browse-edgar?action=getcompany&amp;CIK=1923624">0001923624</a>   FIDELITY DIVERSIFYING SOLUTIONS LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1286320">0001286320</a>   FIDELITY DIVIDEND CAPITAL INC
<a href="browse-edgar?action=getcompany&amp;CIK=1348831">0001348831</a>   VANGUARD 2005 DRILLING &amp; DEVELOPMENT PROGRAM
<a href="browse-edgar?action=getcompany&amp;CIK=891190">0000891190</a>   VANGUARD ADMIRAL FUNDS
<a href="browse-edgar?action=getcompany&amp;CIK=891190">0000891190</a>   VANGUARD ADMIRAL FUNDS INC
<a href="browse-edgar?action=getcompany&amp;CIK=947529">0000947529</a>   VANGUARD ADVISERS INC
<a href="browse-edgar?action=getcompany&amp;CIK=947529">0000947529</a>   VANGUARD ADVISERS INC /ADV
<a href="browse-edgar?action=getcompany&amp;CIK=1000578">0001000578</a>   VANGUARD AIRLINES INC \DE\
<a href="browse-edgar?action=getcompany&amp;CIK=1258324">0001258324</a>   VANGUARD ANIMATION LLC
<a href="browse-edgar?action=getcompany&amp;CIK=836906">0000836906</a>   VANGUARD ASSET ALLOCATION FUND INC
<a href="browse-edgar?action=getcompany&amp;CIK=1680208">0001680208</a>   VANGUARD ASSET MANAGEMENT, LTD
<a href="browse-edgar?action=getcompany&amp;CIK=836724">0000836724</a>   VANGUARD ASSOCIATES III L P
<a href="browse-edgar?action=getcompany&amp;CIK=1054810">0001054810</a>   VANGUARD ATLANTIC LTD
<a href="browse-edgar?action=getcompany&amp;CIK=889519">0000889519</a>   VANGUARD BALANCED INDEX FUND
<a href="browse-edgar?action=getcompany&amp;CIK=889519">0000889519</a>   VANGUARD BALANCED INDEX FUND INC
<a href="browse-edgar?action=getcompany&amp;CIK=889519">0000889519</a>   VANGUARD BALANCED INDEX FUNDS
<a href="browse-edgar?action=getcompany&amp;CIK=1674731">0001674731</a>   VANGUARD BEACHWOOD APARTMENTS, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=794105">0000794105</a>   VANGUARD BOND INDEX FUND INC
<a href="browse-edgar?action=getcompany&amp;CIK=794105">0000794105</a>   VANGUARD BOND INDEX FUNDS
<a href="browse-edgar?action=getcompany&amp;CIK=783401">0000783401</a>   VANGUARD CALIFORNIA TAX FREE FUND
<a href="browse-edgar?action=getcompany&amp;CIK=783401">0000783401</a>   VANGUARD CALIFORNIA TAX FREE FUNDS
<a href="browse-edgar?action=getcompany&amp;CIK=783401">0000783401</a>   VANGUARD CALIFORNIA TAX-FREE FUNDS
<a href="browse-edgar?action=getcompany&amp;CIK=830288">0000830288</a>   VANGUARD CAPITAL    
<a href="browse-edgar?action=getcompany&amp;CIK=830288">0000830288</a>   VANGUARD CAPITAL /BD
<a href="browse-edgar?action=getcompany&amp;CIK=1730578">0001730578</a>   VANGUARD CAPITAL WEALTH ADVISORS
<a href="browse-edgar?action=getcompany&amp;CIK=1326170">0001326170</a>   VANGUARD CAPITAL, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1370828">0001370828</a>   VANGUARD CAR RENTAL GROUP INC.
<a href="browse-edgar?action=getcompany&amp;CIK=1273878">0001273878</a>   VANGUARD CASH MANAGEMENT TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=771178">0000771178</a>   VANGUARD CELLULAR SYSTEMS INC
<a href="browse-edgar?action=getcompany&amp;CIK=1532203">0001532203</a>   VANGUARD CHARLOTTE FUNDS
<a href="browse-edgar?action=getcompany&amp;CIK=752177">0000752177</a>   VANGUARD CHESTER FUNDS
<a href="browse-edgar?action=getcompany&amp;CIK=1284858">0001284858</a>   VANGUARD CHESTER FUNDS
<a href="browse-edgar?action=getcompany&amp;CIK=1273878">0001273878</a>   VANGUARD CMT FUNDS  
<a href="browse-edgar?action=getcompany&amp;CIK=791107">0000791107</a>   VANGUARD CONVERTIBLE SECURITIES FUND
<a href="browse-edgar?action=getcompany&amp;CIK=791107">0000791107</a>   VANGUARD CONVERTIBLE SECURITIES FUND INC
<a href="browse-edgar?action=getcompany&amp;CIK=1683428">0001683428</a>   VANGUARD DEALER SERVICES, L.L.C.
<a href="browse-edgar?action=getcompany&amp;CIK=1497649">0001497649</a>   VANGUARD ENERGY CORP
<a href="browse-edgar?action=getcompany&amp;CIK=1321511">0001321511</a>   VANGUARD ENERGY GROUP, INC.
<a href="browse-edgar?action=getcompany&amp;CIK=826473">0000826473</a>   VANGUARD EQUITY INCOME FUND INC
<a href="browse-edgar?action=getcompany&amp;CIK=1340295">0001340295</a>   VANGUARD EXPLORATION CORP
<a href="browse-edgar?action=getcompany&amp;CIK=34066">0000034066</a>   VANGUARD EXPLORER FUND
<a href="browse-edgar?action=getcompany&amp;CIK=34066">0000034066</a>   VANGUARD EXPLORER FUND INC
<a href="browse-edgar?action=getcompany&amp;CIK=1142637">0001142637</a>   VANGUARD EXTENDED STOCK MAKET INDEX FUND
<a href="browse-edgar?action=getcompany&amp;CIK=1841609">0001841609</a>   VANGUARD FARMS INTERNATIONAL INC
<a href="browse-edgar?action=getcompany&amp;CIK=826473">0000826473</a>   VANGUARD FENWAY FUNDS
<a href="browse-edgar?action=getcompany&amp;CIK=1130926">0001130926</a>   VANGUARD FENWAY FUNDS
<a href="browse-edgar?action=getcompany&amp;CIK=933478">0000933478</a>   VANGUARD FIDUCIARY TRUST CO
<a href="browse-edgar?action=getcompany&amp;CIK=1603857">0001603857</a>   VANGUARD FINANCIAL TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=106444">0000106444</a>   VANGUARD FIXED INCOME SECURITIES FUND INC
<a href="browse-edgar?action=getcompany&amp;CIK=106444">0000106444</a>   VANGUARD FIXED INCOME SECURITIES FUNDS
<a href="browse-edgar?action=getcompany&amp;CIK=888451">0000888451</a>   VANGUARD FLORIDA INSURED TAX FREE FUND
<a href="browse-edgar?action=getcompany&amp;CIK=1174321">0001174321</a>   VANGUARD FLORIDA TAX FREE FUNDS
<a href="browse-edgar?action=getcompany&amp;CIK=888451">0000888451</a>   VANGUARD FLORIDA TAX-FREE FUND
<a href="browse-edgar?action=getcompany&amp;CIK=888451">0000888451</a>   VANGUARD FLORIDA TAX-FREE FUNDS
<a href="browse-edgar?action=getcompany&amp;CIK=1811242">0001811242</a>   VANGUARD GLOBAL ADVISERS, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=2013071">0002013071</a>   VANGUARD GOLD CAPITAL INC
<a href="browse-edgar?action=getcompany&amp;CIK=1746119">0001746119</a>   VANGUARD GREEN INVESTMENT LTD
<a href="browse-edgar?action=getcompany&amp;CIK=102909">0000102909</a>   VANGUARD GROUP INC  
<a href="browse-edgar?action=getcompany&amp;CIK=735286">0000735286</a>   VANGUARD GROUP INC  
<a href="browse-edgar?action=getcompany&amp;CIK=735286">0000735286</a>   VANGUARD GROUP INC /TA
<a href="browse-edgar?action=getcompany&amp;CIK=1807289">0001807289</a>   VANGUARD HARBOURVEST 2020 PRIVATE EQUITY FEEDER FUND L.P.
<a href="browse-edgar?action=getcompany&amp;CIK=1807286">0001807286</a>   VANGUARD HARBOURVEST 2020 PRIVATE EQUITY FUND L.P.
<a href="browse-edgar?action=getcompany&amp;CIK=1871481">0001871481</a>   VANGUARD HARBOURVEST 2021 PRIVATE EQUITY FEEDER FUND L.P.
<a href="browse-edgar?action=getcompany&amp;CIK=1871477">0001871477</a>   VANGUARD HARBOURVEST 2021 PRIVATE EQUITY FUND L.P.
<a href="browse-edgar?action=getcompany&amp;CIK=2020059">0002020059</a>   VANGUARD HARBOURVEST 2021 PRIVATE EQUITY HOLDINGS LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1920881">0001920881</a>   VANGUARD HARBOURVEST 2022 PRIVATE EQUITY FEEDER FUND L.P.
<a href="browse-edgar?action=getcompany&amp;CIK=1920852">0001920852</a>   VANGUARD HARBOURVEST 2022 PRIVATE EQUITY FUND L.P.
<a href="browse-edgar?action=getcompany&amp;CIK=2020058">0002020058</a>   VANGUARD HARBOURVEST 2022 PRIVATE EQUITY HOLDINGS LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1958781">0001958781</a>   VANGUARD HARBOURVEST 2023 PRIVATE EQUITY FEEDER FUND L.P.
<a href="browse-edgar?action=getcompany&amp;CIK=1958768">0001958768</a>   VANGUARD HARBOURVEST 2023 PRIVATE EQUITY FUND L.P.
<a href="browse-edgar?action=getcompany&amp;CIK=2014811">0002014811</a>   VANGUARD HARBOURVEST 2024 PRIVATE EQUITY FEEDER FUND L.P.
<a href="browse-edgar?action=getcompany&amp;CIK=2014810">0002014810</a>   VANGUARD HARBOURVEST 2024 PRIVATE EQUITY FUND L.P.
<a href="browse-edgar?action=getcompany&amp;CIK=2049251">0002049251</a>   VANGUARD HARBOURVEST 2025 PRIVATE EQUITY FUND L.P.
<a href="browse-edgar?action=getcompany&amp;CIK=1161106">0001161106</a>   VANGUARD HEALTH FINANCIAL CO INC
<a href="browse-edgar?action=getcompany&amp;CIK=1161106">0001161106</a>   VANGUARD HEALTH FINANCIAL CO LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1307389">0001307389</a>   VANGUARD HEALTH HOLDING CO I, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1307411">0001307411</a>   VANGUARD HEALTH HOLDING CO II, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1161103">0001161103</a>   VANGUARD HEALTH MANAGEMENT INC
<a href="browse-edgar?action=getcompany&amp;CIK=1045829">0001045829</a>   VANGUARD HEALTH SYSTEMS INC
<a href="browse-edgar?action=getcompany&amp;CIK=2053841">0002053841</a>   VANGUARD HIGHGROWTH FUND LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1307399">0001307399</a>   VANGUARD HOLDING CO I, INC.
<a href="browse-edgar?action=getcompany&amp;CIK=1307400">0001307400</a>   VANGUARD HOLDING CO II, INC.
<a href="browse-edgar?action=getcompany&amp;CIK=1731565">0001731565</a>   VANGUARD HOLDING COMPANY, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1649293">0001649293</a>   VANGUARD HOLDING CORP.
<a href="browse-edgar?action=getcompany&amp;CIK=932471">0000932471</a>   VANGUARD HORIZON FUND INC
<a href="browse-edgar?action=getcompany&amp;CIK=932471">0000932471</a>   VANGUARD HORIZON FUNDS
<a href="browse-edgar?action=getcompany&amp;CIK=1380307">0001380307</a>   VANGUARD IMAGING PARTNERS LLC
<a href="browse-edgar?action=getcompany&amp;CIK=36405">0000036405</a>   VANGUARD INDEX FUNDS
<a href="browse-edgar?action=getcompany&amp;CIK=1114857">0001114857</a>   VANGUARD INDEX FUNDS
<a href="browse-edgar?action=getcompany&amp;CIK=36405">0000036405</a>   VANGUARD INDEX FUNDS/
<a href="browse-edgar?action=getcompany&amp;CIK=36405">0000036405</a>   VANGUARD INDEX TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=862084">0000862084</a>   VANGUARD INSTITUTIONAL INDEX FUND
<a href="browse-edgar?action=getcompany&amp;CIK=862084">0000862084</a>   VANGUARD INSTITUTIONAL INDEX FUNDS
<a href="browse-edgar?action=getcompany&amp;CIK=846591">0000846591</a>   VANGUARD INSTITUTIONAL PORTFOLIOS INC
<a href="browse-edgar?action=getcompany&amp;CIK=1104225">0001104225</a>   VANGUARD INSURANCE AGENCY INC
<a href="browse-edgar?action=getcompany&amp;CIK=857489">0000857489</a>   VANGUARD INTERNATIONAL EQUITY INDEX FUND INC
<a href="browse-edgar?action=getcompany&amp;CIK=857489">0000857489</a>   VANGUARD INTERNATIONAL EQUITY INDEX FUNDS
<a href="browse-edgar?action=getcompany&amp;CIK=1305589">0001305589</a>   VANGUARD INVESTMENT EUROPE SA
<a href="browse-edgar?action=getcompany&amp;CIK=1898388">0001898388</a>   VANGUARD INVESTMENT HOLDINGS ONE (CAYMAN) L.P.
<a href="browse-edgar?action=getcompany&amp;CIK=1599779">0001599779</a>   VANGUARD INVESTMENT SERIES PLC
<a href="browse-edgar?action=getcompany&amp;CIK=1550100">0001550100</a>   VANGUARD INVESTMENTS AUSTRALIA, LTD.
<a href="browse-edgar?action=getcompany&amp;CIK=1016735">0001016735</a>   VANGUARD IV L P
<a href="browse-edgar?action=getcompany&amp;CIK=1483438">0001483438</a>   BLACKROCK (ISLE OF MAN) LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1426606">0001426606</a>   BLACKROCK (LUXEMBOURG) S.A.
<a href="browse-edgar?action=getcompany&amp;CIK=1388399">0001388399</a>   BLACKROCK (NETHERLANDS) B.V.
<a href="browse-edgar?action=getcompany&amp;CIK=1559921">0001559921</a>   BLACKROCK (SINGAPORE) LTD.
<a href="browse-edgar?action=getcompany&amp;CIK=872604">0000872604</a>   BLACKROCK 1998 TERM TRUST INC
<a href="browse-edgar?action=getcompany&amp;CIK=893731">0000893731</a>   BLACKROCK 1999 TERM TRUST INC
<a href="browse-edgar?action=getcompany&amp;CIK=889127">0000889127</a>   BLACKROCK 2001 TERM TRUST INC
<a href="browse-edgar?action=getcompany&amp;CIK=1126797">0001126797</a>   BLACKROCK 2012 TERM TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=1911258">0001911258</a>   BLACKROCK 2019 EVERGREEN PRIVATE OPPORTUNITIES CAYMAN MASTER LTD.
<a href="browse-edgar?action=getcompany&amp;CIK=1861663">0001861663</a>   BLACKROCK 2019 EVERGREEN PRIVATE OPPORTUNITIES FEEDER SCSP
<a href="browse-edgar?action=getcompany&amp;CIK=1861665">0001861665</a>   BLACKROCK 2019 EVERGREEN PRIVATE OPPORTUNITIES MASTER SCSP
<a href="browse-edgar?action=getcompany&amp;CIK=1691433">0001691433</a>   BLACKROCK 2022 GLOBAL INCOME OPPORTUNITY TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=2004914">0002004914</a>   BLACKROCK 2023 A SERIES OF WHAT IF VENTURES MASTER LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1832871">0001832871</a>   BLACKROCK 2037 MUNICIPAL TARGET TERM TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=1982067">0001982067</a>   BLACKROCK 2038 MUNICIPAL TARGET TERM TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=1832871">0001832871</a>   BLACKROCK 2040 MUNICIPAL TARGET TERM TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=1898709">0001898709</a>   BLACKROCK ABSOLUTE MACRO FUND LTD.
<a href="browse-edgar?action=getcompany&amp;CIK=1806252">0001806252</a>   BLACKROCK ABSOLUTE RETURN FUND, LTD.
<a href="browse-edgar?action=getcompany&amp;CIK=1314988">0001314988</a>   BLACKROCK ABSOLUTE RETURN PARTNERS (OFFSHORE) LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1314988">0001314988</a>   BLACKROCK ABSOLUTE RETURN PARTNERS LTD
<a href="browse-edgar?action=getcompany&amp;CIK=922457">0000922457</a>   BLACKROCK ADVANTAGE GLOBAL FUND, INC.
<a href="browse-edgar?action=getcompany&amp;CIK=230382">0000230382</a>   BLACKROCK ADVANTAGE SMID CAP FUND, INC.
<a href="browse-edgar?action=getcompany&amp;CIK=845851">0000845851</a>   BLACKROCK ADVANTAGE TERM TRUST INC
<a href="browse-edgar?action=getcompany&amp;CIK=230382">0000230382</a>   BLACKROCK ADVANTAGE U.S. TOTAL MARKET FUND, INC.
<a href="browse-edgar?action=getcompany&amp;CIK=1034551">0001034551</a>   BLACKROCK ADVISORS (UK) LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1086364">0001086364</a>   BLACKROCK ADVISORS INC
<a href="browse-edgar?action=getcompany&amp;CIK=1086364">0001086364</a>   BLACKROCK ADVISORS LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1578761">0001578761</a>   BLACKROCK ALL ASSET INCOME TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=1221845">0001221845</a>   BLACKROCK ALLOCATION TARGET SHARES
<a href="browse-edgar?action=getcompany&amp;CIK=1833936">0001833936</a>   BLACKROCK ALPHA STRATEGIES FUND
<a href="browse-edgar?action=getcompany&amp;CIK=1403238">0001403238</a>   BLACKROCK ALTERNATIVE ENERGY &amp; RESOURCE TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=1980233">0001980233</a>   BLACKROCK ALTERNATIVE FUNDS II ELTIF SICAV - BLACKROCK PRIVATE EQUITY ELTIF
<a href="browse-edgar?action=getcompany&amp;CIK=1913942">0001913942</a>   BLACKROCK ALTERNATIVE FUNDS S.C.A., SICAV-RAIF - BLACKROCK PRIVATE EQUITY IMPACT OPPORTUNITIES ELTIF
<a href="browse-edgar?action=getcompany&amp;CIK=1529140">0001529140</a>   BLACKROCK ALTERNATIVES ALLOCATION FB PORTFOLIO LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1529139">0001529139</a>   BLACKROCK ALTERNATIVES ALLOCATION FB TEI PORTFOLIO LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1529138">0001529138</a>   BLACKROCK ALTERNATIVES ALLOCATION MASTER PORTFOLIO LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1529142">0001529142</a>   BLACKROCK ALTERNATIVES ALLOCATION PORTFOLIO LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1529141">0001529141</a>   BLACKROCK ALTERNATIVES ALLOCATION TEI PORTFOLIO LLC
<a href="browse-edgar?action=getcompany&amp;CIK=817998">0000817998</a>   BLACKROCK APEX MUNICIPAL FUND INC
<a href="browse-edgar?action=getcompany&amp;CIK=1861666">0001861666</a>   BLACKROCK APO GLOBAL HEALTHCARE PRIVATE EQUITY FUND, S.C.A. SICAV-RAIF
<a href="browse-edgar?action=getcompany&amp;CIK=1355386">0001355386</a>   BLACKROCK APPRECIATION ASP FUND, A SERIES OF ALTERNATIVE STRATEGIES PLATFORM, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1478205">0001478205</a>   BLACKROCK APPRECIATION FUND IV (ERISA), LTD.
<a href="browse-edgar?action=getcompany&amp;CIK=1480559">0001480559</a>   BLACKROCK APPRECIATION FUND IV, LTD.
<a href="browse-edgar?action=getcompany&amp;CIK=1172916">0001172916</a>   BLACKROCK APPRECIATION STRATEGY FUND, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1480559">0001480559</a>   BLACKROCK APPRECIATION STRATEGY FUND, LTD.
<a href="browse-edgar?action=getcompany&amp;CIK=1876254">0001876254</a>   BLACKROCK ASF PRIVATE OPPORTUNITIES FUND, L.P.
<a href="browse-edgar?action=getcompany&amp;CIK=1320158">0001320158</a>   BLACKROCK ASIA PACIFIC PARTNERS (OFFSHORE) LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1320158">0001320158</a>   BLACKROCK ASIA PACIFIC PARTNERS (OFFSHORE) LTD.
<a href="browse-edgar?action=getcompany&amp;CIK=1404876">0001404876</a>   BLACKROCK ASIA PACIFIC PARTNERS LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1404876">0001404876</a>   BLACKROCK ASIA PACIFIC PARTNERS LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1320158">0001320158</a>   BLACKROCK ASIA PACIFIC PARTNERS LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1835413">0001835413</a>   BLACKROCK ASIA PROPERTY FUND V (2) SCSP
<a href="browse-edgar?action=getcompany&amp;CIK=2002446">0002002446</a>   BLACKROCK ASIA PROPERTY FUND VI SCSP
<a href="browse-edgar?action=getcompany&amp;CIK=1865041">0001865041</a>   BLACKROCK ASIA-PACIFIC PRIVATE CREDIT OPP. FUND II (DE FEEDER) LP
<a href="browse-edgar?action=getcompany&amp;CIK=202741">0000202741</a>   BLACKROCK ASIAN DRAGON FUND, INC.
<a href="browse-edgar?action=getcompany&amp;CIK=939377">0000939377</a>   BLACKROCK ASSET INVESTORS
<a href="browse-edgar?action=getcompany&amp;CIK=1417008">0001417008</a>   BLACKROCK ASSET MANAGEMENT AUSTRALIA LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1050459">0001050459</a>   BLACKROCK ASSET MANAGEMENT CANADA LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1415064">0001415064</a>   BLACKROCK ASSET MANAGEMENT DEUTSCHLAND AG
<a href="browse-edgar?action=getcompany&amp;CIK=1579406">0001579406</a>   BLACKROCK ASSET MANAGEMENT INTERNATIONAL INC
<a href="browse-edgar?action=getcompany&amp;CIK=1503309">0001503309</a>   BLACKROCK ASSET MANAGEMENT IRELAND LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1579409">0001579409</a>   BLACKROCK ASSET MANAGEMENT NORTH ASIA LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1483440">0001483440</a>   BLACKROCK ASSET MANAGEMENT PENSIONS LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1654470">0001654470</a>   BLACKROCK ASSET MANAGEMENT SCHWEIZ AG
<a href="browse-edgar?action=getcompany&amp;CIK=1388404">0001388404</a>   BLACKROCK ASSET MANAGEMENT UK LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1911289">0001911289</a>   BLACKROCK BAKER CLO 2021-1, LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1911287">0001911287</a>   BLACKROCK BAKER CLO VIII, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=110055">0000110055</a>   BLACKROCK BALANCED CAPITAL FUND, INC.
<a href="browse-edgar?action=getcompany&amp;CIK=110055">0000110055</a>   BLACKROCK BALANCED FUND, INC.
<a href="browse-edgar?action=getcompany&amp;CIK=1208195">0001208195</a>   BLACKROCK BALANCED PARTNERS TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=2062508">0002062508</a>   BLACKROCK BANK CAPITAL AWARE INCOME FUND SERIES INTERESTS OF THE SALI SVW MULTI-SERIES FUND, L.P.
<a href="browse-edgar?action=getcompany&amp;CIK=1114698">0001114698</a>   BLACKROCK BASIC VALUE FUND II, INC
<a href="browse-edgar?action=getcompany&amp;CIK=216557">0000216557</a>   BLACKROCK BASIC VALUE FUND, INC.
<a href="browse-edgar?action=getcompany&amp;CIK=1221845">0001221845</a>   BLACKROCK BOND ALLOCATION TARGET SHARES
<a href="browse-edgar?action=getcompany&amp;CIK=276463">0000276463</a>   BLACKROCK BOND FUND, INC.
<a href="browse-edgar?action=getcompany&amp;CIK=1883064">0001883064</a>   BLACKROCK BOWLING GREEN HEDGE FUND OF FUNDS, L.P.
<a href="browse-edgar?action=getcompany&amp;CIK=1579408">0001579408</a>   BLACKROCK BRASIL GESTORA DE INVESTIMENTOS LTD.
<a href="browse-edgar?action=getcompany&amp;CIK=1592341">0001592341</a>   BLACKROCK BREWERS   
<a href="browse-edgar?action=getcompany&amp;CIK=892789">0000892789</a>   BLACKROCK BROAD INVESTMENT GRADE 2009 TERM TRUST INC
<a href="browse-edgar?action=getcompany&amp;CIK=1938881">0001938881</a>   BLACKROCK BROADWAY FUND, L.P.
<a href="browse-edgar?action=getcompany&amp;CIK=1493683">0001493683</a>   BLACKROCK BUILD AMERICA BOND TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=890514">0000890514</a>   BLACKROCK CALIFORNIA INSURED MUNICIPAL 2008 TERM TRUST INC
<a href="browse-edgar?action=getcompany&amp;CIK=1181027">0001181027</a>   BLACKROCK CALIFORNIA INSURED MUNICIPAL INCOME TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=902722">0000902722</a>   BLACKROCK CALIFORNIA INVESTMENT QUALITY MUNICIPAL TRUST INC
<a href="browse-edgar?action=getcompany&amp;CIK=1159038">0001159038</a>   BLACKROCK CALIFORNIA MUNICIPAL 2018 TERM TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=1181248">0001181248</a>   BLACKROCK CALIFORNIA MUNICIPAL 2020 TERM TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=1181248">0001181248</a>   BLACKROCK CALIFORNIA MUNICIPAL 2022 TERM TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=1169027">0001169027</a>   BLACKROCK CALIFORNIA MUNICIPAL BOND TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=1137391">0001137391</a>   BLACKROCK CALIFORNIA MUNICIPAL INCOME TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=1176196">0001176196</a>   BLACKROCK CALIFORNIA MUNICIPAL INCOME TRUST II
<a href="browse-edgar?action=getcompany&amp;CIK=1181027">0001181027</a>   BLACKROCK CALIFORNIA MUNICIPAL INCOME TRUST III
<a href="browse-edgar?action=getcompany&amp;CIK=765199">0000765199</a>   BLACKROCK CALIFORNIA MUNICIPAL SERIES TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=1278895">0001278895</a>   BLACKROCK CAPITAL &amp; INCOME STRATEGIES FUND INC
<a href="browse-edgar?action=getcompany&amp;CIK=1809541">0001809541</a>   BLACKROCK CAPITAL ALLOCATION TERM TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=1809541">0001809541</a>   BLACKROCK CAPITAL ALLOCATION TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=887509">0000887509</a>   BLACKROCK CAPITAL APPRECIATION FUND, INC.
<a href="browse-edgar?action=getcompany&amp;CIK=1717705">0001717705</a>   BLACKROCK CAPITAL INVESTMENT ADVISORS, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1326003">0001326003</a>   BLACKROCK CAPITAL INVESTMENT CORP
<a href="browse-edgar?action=getcompany&amp;CIK=1173486">0001173486</a>   BLACKROCK CAPITAL MANAGEMENT INC
<a href="browse-edgar?action=getcompany&amp;CIK=1374182">0001374182</a>   BLACKROCK CAPITAL MANAGEMENT INC.
<a href="browse-edgar?action=getcompany&amp;CIK=1167281">0001167281</a>   JP MORGAN 2001 POOL PARTICIPATION FUND FOUNDATION LP
<a href="browse-edgar?action=getcompany&amp;CIK=1286410">0001286410</a>   JP MORGAN ACCESS MULTI-STRATEGY FUND LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1516637">0001516637</a>   JP MORGAN AG / TA   
<a href="browse-edgar?action=getcompany&amp;CIK=1459954">0001459954</a>   JP MORGAN ALPHA FUND LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1257211">0001257211</a>   JP MORGAN ALTERNATIVE ASSET MANAGEMENT INC
<a href="browse-edgar?action=getcompany&amp;CIK=1342561">0001342561</a>   JP MORGAN ASSET MANAGEMENT LONDON LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1266796">0001266796</a>   JP MORGAN CAPITAL CORP
<a href="browse-edgar?action=getcompany&amp;CIK=1317550">0001317550</a>   JP MORGAN CAPITAL LP
<a href="browse-edgar?action=getcompany&amp;CIK=1329950">0001329950</a>   JP MORGAN CAPITAL MANAGEMENT CO LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1388848">0001388848</a>   JP MORGAN CAPITAL MANAGEMENT COMPANY, L.P.
<a href="browse-edgar?action=getcompany&amp;CIK=1168163">0001168163</a>   JP MORGAN CHASE &amp; CO
<a href="browse-edgar?action=getcompany&amp;CIK=1170968">0001170968</a>   JP MORGAN CHASE &amp; CO
<a href="browse-edgar?action=getcompany&amp;CIK=1171321">0001171321</a>   JP MORGAN CHASE &amp; CO
<a href="browse-edgar?action=getcompany&amp;CIK=1208636">0001208636</a>   JP MORGAN CHASE BANK
<a href="browse-edgar?action=getcompany&amp;CIK=1327421">0001327421</a>   JP MORGAN CHASE BANK NA
<a href="browse-edgar?action=getcompany&amp;CIK=1209192">0001209192</a>   JP MORGAN CHASE COM MORT SEC CORP PAS THR CER SER 2002-C2
<a href="browse-edgar?action=getcompany&amp;CIK=1198813">0001198813</a>   JP MORGAN CHASE COM MORT SEC CORP PAS THR CRT SER 2002 CIBC5
<a href="browse-edgar?action=getcompany&amp;CIK=1206251">0001206251</a>   JP MORGAN CHASE COM MORT SEC CORP PASS THR CE SE 2002-C2
<a href="browse-edgar?action=getcompany&amp;CIK=1223146">0001223146</a>   JP MORGAN CHASE COM MORT SEC CORP PASS THR CERT SE 2003 C1
<a href="browse-edgar?action=getcompany&amp;CIK=1264059">0001264059</a>   JP MORGAN CHASE COM MORT SEC CORP PS THR CERTS SER 2003-LN1
<a href="browse-edgar?action=getcompany&amp;CIK=1209655">0001209655</a>   JP MORGAN CHASE COM MORT SEC CORP PT CERTS SERIES 02 C3
<a href="browse-edgar?action=getcompany&amp;CIK=1256074">0001256074</a>   JP MORGAN CHASE COM SEC CORP PASS THRU CERT SER 2003-CIBC6
<a href="browse-edgar?action=getcompany&amp;CIK=1179904">0001179904</a>   JP MORGAN CHASE COMM MOR SEC CORP MOR PAS THR CE SE 2002-C1
<a href="browse-edgar?action=getcompany&amp;CIK=1171484">0001171484</a>   JP MORGAN CHASE COMM MORT PASS THR CERTS SER 2002 CIBC4
<a href="browse-edgar?action=getcompany&amp;CIK=1270815">0001270815</a>   JP MORGAN CHASE COMM MORT PASS THR CERTS SER 2003-CIBC7
<a href="browse-edgar?action=getcompany&amp;CIK=1260907">0001260907</a>   JP MORGAN CHASE COMM MORT PASS THR CERTS SER 2003-PM1
<a href="browse-edgar?action=getcompany&amp;CIK=1163449">0001163449</a>   JP MORGAN CHASE COMMERCIAL MORT SEC CORP SERIES 2001-CIBC3
<a href="browse-edgar?action=getcompany&amp;CIK=1136857">0001136857</a>   JP MORGAN CHASE COMMERCIAL MORT SEC CORP SERIES 2001-CIBCI
<a href="browse-edgar?action=getcompany&amp;CIK=1013611">0001013611</a>   JP MORGAN CHASE COMMERCIAL MORTGAGE SECURITIES CORP
<a href="browse-edgar?action=getcompany&amp;CIK=1349681">0001349681</a>   JP MORGAN CHASE COMMERCIAL MORTGAGE SECURITIES TRUST 2006-CIBC14
<a href="browse-edgar?action=getcompany&amp;CIK=1354045">0001354045</a>   JP MORGAN CHASE COMMERCIAL MORTGAGE SECURITIES TRUST 2006-LDP6
<a href="browse-edgar?action=getcompany&amp;CIK=1145066">0001145066</a>   JP MORGAN CHASE COMMERICAL MORT SEC CORP SERIES 2001-CIB02
<a href="browse-edgar?action=getcompany&amp;CIK=1110666">0001110666</a>   JP MORGAN COMMERCIAL MORT FIN CORP PASS THR CERT SER 99 C8
<a href="browse-edgar?action=getcompany&amp;CIK=1279249">0001279249</a>   JP MORGAN COMMERCIAL MORT PASS THR CERTS SER 2004-C1
<a href="browse-edgar?action=getcompany&amp;CIK=1413441">0001413441</a>   JP MORGAN CORPORATE FINANCE PRIVATE INVESTORS III OFFSHORE SPECIAL LP
<a href="browse-edgar?action=getcompany&amp;CIK=1164130">0001164130</a>   JP MORGAN CORSAIR II CAPITAL PARTNERS LP
<a href="browse-edgar?action=getcompany&amp;CIK=1349745">0001349745</a>   JP MORGAN DIRECT VENTURE CAPITAL INSTITUTIONAL INVESTORS III LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1092079">0001092079</a>   JP MORGAN DIRECT VENTURE CAPITAL INSTITUTIONAL INVESTORS LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1092077">0001092077</a>   JP MORGAN DIRECT VENTURE CAPITAL PRIVATE INVESTORS LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1188642">0001188642</a>   JP MORGAN EUROPEAN DIRECT CORP FIN INST INVESTORS II LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1228440">0001228440</a>   JP MORGAN EUROPEAN DIRECT CORP FIN PRIVATE INVESTORS II LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1349746">0001349746</a>   JP MORGAN EUROPEAN DIRECT CORPORATE FINANCE INSTITUTIONAL INVESTORS III LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1188637">0001188637</a>   JP MORGAN EUROPEAN POOLED CORP FIN INST INVESTORS II LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1228436">0001228436</a>   JP MORGAN EUROPEAN POOLED CORP FIN PRIVATE INVESTORS II LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1349740">0001349740</a>   JP MORGAN EUROPEAN POOLED CORPORATE FINANCE INSTITUTIONAL INVESTORS III LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1349742">0001349742</a>   JP MORGAN EUROPEAN POOLED VENTURE CAPITAL INSTITUTIONAL INVESTORS III LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1145427">0001145427</a>   JP MORGAN FLEMING ASSET MANAGEMENT LONDON LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1144599">0001144599</a>   JP MORGAN FLEMING ASSET MANAGEMENT USA INC
<a href="browse-edgar?action=getcompany&amp;CIK=1037897">0001037897</a>   JP MORGAN FLEMING MUTUAL FUND GROUP INC
<a href="browse-edgar?action=getcompany&amp;CIK=1212767">0001212767</a>   JP MORGAN FLEMING SERIES TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=894089">0000894089</a>   JP MORGAN FUNDS     
<a href="browse-edgar?action=getcompany&amp;CIK=1384001">0001384001</a>   JP MORGAN IIF ERISA LP
<a href="browse-edgar?action=getcompany&amp;CIK=1384002">0001384002</a>   JP MORGAN IIF LP    
<a href="browse-edgar?action=getcompany&amp;CIK=1384000">0001384000</a>   JP MORGAN IIF TAX-EXEMPT LP
<a href="browse-edgar?action=getcompany&amp;CIK=1221491">0001221491</a>   JP MORGAN INCUBATOR FUND LP
<a href="browse-edgar?action=getcompany&amp;CIK=894088">0000894088</a>   JP MORGAN INSTITUTIONAL FUNDS
<a href="browse-edgar?action=getcompany&amp;CIK=880391">0000880391</a>   JP MORGAN INVESTMENT ADVISORS INC.
<a href="browse-edgar?action=getcompany&amp;CIK=1173475">0001173475</a>   JP MORGAN INVESTMENT MANAGEMENT INC
<a href="browse-edgar?action=getcompany&amp;CIK=741611">0000741611</a>   JP MORGAN INVESTMENT MANAGEMENT INC /ADV
<a href="browse-edgar?action=getcompany&amp;CIK=928121">0000928121</a>   JP MORGAN INVESTMENT MANAGEMENT, INC.
<a href="browse-edgar?action=getcompany&amp;CIK=1145894">0001145894</a>   JP MORGAN INVESTOR SERVICES CO
<a href="browse-edgar?action=getcompany&amp;CIK=1271370">0001271370</a>   JP MORGAN MORTGAGE TRUST 2003-A2
<a href="browse-edgar?action=getcompany&amp;CIK=1281190">0001281190</a>   JP MORGAN MORTGAGE TRUST 2004-A1 MORT PASS THRU CERTS
<a href="browse-edgar?action=getcompany&amp;CIK=1177988">0001177988</a>   JP MORGAN MOSAIC FUND VI LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1460006">0001460006</a>   JP MORGAN MSF II LP ACCESS FUND LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1460027">0001460027</a>   JP MORGAN MULTI-STRATEGY FUND II LP
<a href="browse-edgar?action=getcompany&amp;CIK=1161000">0001161000</a>   JP MORGAN MULTI-STRATEGY FUND II LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1286410">0001286410</a>   JP MORGAN MULTI-STRATEGY FUND LLC
<a href="browse-edgar?action=getcompany&amp;CIK=814078">0000814078</a>   JP MORGAN MUTUAL FUND GROUP/MA
<a href="browse-edgar?action=getcompany&amp;CIK=803747">0000803747</a>   JP MORGAN MUTUAL FUND INVESTMENT TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=1023771">0001023771</a>   JP MORGAN MUTUAL FUND SELECT GROUP
<a href="browse-edgar?action=getcompany&amp;CIK=1023772">0001023772</a>   JP MORGAN MUTUAL FUND SELECT TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=1217286">0001217286</a>   JP MORGAN MUTUAL FUND SERIES
<a href="browse-edgar?action=getcompany&amp;CIK=919034">0000919034</a>   JP MORGAN MUTUAL FUND TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=1173303">0001173303</a>   JP MORGAN NEW CENTURY FUND LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1106535">0001106535</a>   JP MORGAN PARTNERS 23A SBIC LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1106535">0001106535</a>   JP MORGAN PARTNERS 23A SBIC LP
<a href="browse-edgar?action=getcompany&amp;CIK=1106607">0001106607</a>   JP MORGAN PARTNERS BHCA LP
<a href="browse-edgar?action=getcompany&amp;CIK=1278277">0001278277</a>   JP MORGAN PARTNERS DJ PARTNERS LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1207802">0001207802</a>   JP MORGAN PARTNERS GLOBAL INVESTORS H &amp; Q EMPLOYEE LP
<a href="browse-edgar?action=getcompany&amp;CIK=1162622">0001162622</a>   JP MORGAN PARTNERS GLOBAL INVESTORS LP
<a href="browse-edgar?action=getcompany&amp;CIK=1282680">0001282680</a>   JP MORGAN PARTNERS GLOBAL INVESTORS SBIC LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1317633">0001317633</a>   JP MORGAN PARTNERS GLOBAL INVESTORS SELLDOWN CAYMAN 111 LP
<a href="browse-edgar?action=getcompany&amp;CIK=1361608">0001361608</a>   JP MORGAN PARTNERS GLOBAL INVESTORS SELLDOWN II L P
<a href="browse-edgar?action=getcompany&amp;CIK=1317638">0001317638</a>   JP MORGAN PARTNERS GLOBAL INVESTORS SELLDOWN LLP
<a href="browse-edgar?action=getcompany&amp;CIK=1317638">0001317638</a>   JP MORGAN PARTNERS GLOBAL INVESTORS SELLDOWN LP
<a href="browse-edgar?action=getcompany&amp;CIK=1015240">0001015240</a>   JP MORGAN PARTNERS SAIC LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1329949">0001329949</a>   JP MORGAN SBIC HOLDINGS LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1317552">0001317552</a>   JP MORGAN SBIC LLC  
<a href="browse-edgar?action=getcompany&amp;CIK=1168524">0001168524</a>   JP MORGAN SECURITIES LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1016937">0001016937</a>   JP MORGAN SERIES TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=916118">0000916118</a>   JP MORGAN SERIES TRUST II
<a href="browse-edgar?action=getcompany&amp;CIK=1499210">0001499210</a>   JP MORGAN TRUST CO (BAHAMAS) LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1183134">0001183134</a>   JP MORGAN US CORPORATE FIN PRIVATE INV II OFFSHORE SPEC LP
<a href="browse-edgar?action=getcompany&amp;CIK=1228104">0001228104</a>   JP MORGAN US DIRECT CORPORATE FIN INSTITUT INVESTOR II LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1183140">0001183140</a>   JP MORGAN US DIRECT CORPORATE FIN PRIVATE INVESTORS II LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1349784">0001349784</a>   JP MORGAN US DIRECT CORPORATE FINANCE INSTITUTIONAL INVESTORS III LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1183139">0001183139</a>   JP MORGAN US POOLED CORPORATE FIN PRIVATE INVESTORS II LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1349783">0001349783</a>   JP MORGAN US POOLED CORPORATE FINANCE INSTITUTIONAL INVESTORS III LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1165124">0001165124</a>   JP MORGAN US REAL ESTATE INCOME &amp; GROWTH DOMESTIC LP
<a href="browse-edgar?action=getcompany&amp;CIK=769993">0000769993</a>   GOLDMAN SACHS &amp; CO
<a href="browse-edgar?action=getcompany&amp;CIK=42352">0000042352</a>   GOLDMAN SACHS &amp; CO /BD
<a href="browse-edgar?action=getcompany&amp;CIK=734700">0000734700</a>   GOLDMAN SACHS &amp; CO /TA
<a href="browse-edgar?action=getcompany&amp;CIK=734700">0000734700</a>   GOLDMAN SACHS &amp; CO /TA
<a href="browse-edgar?action=getcompany&amp;CIK=1098457">0001098457</a>   GOLDMAN SACHS &amp; CO BANK
<a href="browse-edgar?action=getcompany&amp;CIK=769993">0000769993</a>   GOLDMAN SACHS &amp; CO ET AL
<a href="browse-edgar?action=getcompany&amp;CIK=1031766">0001031766</a>   GOLDMAN SACHS &amp; CO OHG
<a href="browse-edgar?action=getcompany&amp;CIK=42352">0000042352</a>   GOLDMAN SACHS &amp; CO. LLC
<a href="browse-edgar?action=getcompany&amp;CIK=769993">0000769993</a>   GOLDMAN SACHS &amp; CO. LLC
<a href="browse-edgar?action=getcompany&amp;CIK=734700">0000734700</a>   GOLDMAN SACHS &amp; CO. LLC /TA
<a href="browse-edgar?action=getcompany&amp;CIK=353765">0000353765</a>   GOLDMAN SACHS &amp; PARTNERS AUSTRALIA INC.
<a href="browse-edgar?action=getcompany&amp;CIK=1828660">0001828660</a>   GOLDMAN SACHS (MALAYSIA) SDN. BHD.
<a href="browse-edgar?action=getcompany&amp;CIK=1117544">0001117544</a>   GOLDMAN SACHS 2000 EXCHANGE PLACE FUND LP
<a href="browse-edgar?action=getcompany&amp;CIK=1206532">0001206532</a>   GOLDMAN SACHS 2002 EXCHANGE PLACE FUND LP
<a href="browse-edgar?action=getcompany&amp;CIK=1293719">0001293719</a>   GOLDMAN SACHS 2004 EXCHANGE PLACE FUND L P
<a href="browse-edgar?action=getcompany&amp;CIK=1333803">0001333803</a>   GOLDMAN SACHS 2005 EXCHANGE PLACE FUND L P
<a href="browse-edgar?action=getcompany&amp;CIK=1364429">0001364429</a>   GOLDMAN SACHS 2006 EXCHANGE PLACE FUND L P
<a href="browse-edgar?action=getcompany&amp;CIK=1420881">0001420881</a>   GOLDMAN SACHS 230 PARK INVESTORS LP
<a href="browse-edgar?action=getcompany&amp;CIK=1270864">0001270864</a>   GOLDMAN SACHS ABSOLUTE RETURN FUND OFFSHORE LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1471043">0001471043</a>   GOLDMAN SACHS ACCESS - GOLDMAN SACHS INVESTMENT PARTNERS/LIBERTY HARBOR, L.P.
<a href="browse-edgar?action=getcompany&amp;CIK=1387257">0001387257</a>   GOLDMAN SACHS ALPHA BETA CONTINUUM ERISA FUND LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1381577">0001381577</a>   GOLDMAN SACHS ALPHA BETA CONTINUUM FUND LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1357753">0001357753</a>   GOLDMAN SACHS ALPHA BETA CONTINUUM FUND LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1360084">0001360084</a>   GOLDMAN SACHS ALPHA-BETA CONTINUUM FUND LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1210198">0001210198</a>   GOLDMAN SACHS ASSET BACKED SECURITIES CORP
<a href="browse-edgar?action=getcompany&amp;CIK=1408886">0001408886</a>   GOLDMAN SACHS ASSET MANAGEMENT CLO PLC
<a href="browse-edgar?action=getcompany&amp;CIK=919361">0000919361</a>   GOLDMAN SACHS ASSET MANAGEMENT INTERNATIONAL
<a href="browse-edgar?action=getcompany&amp;CIK=1229262">0001229262</a>   GOLDMAN SACHS ASSET MANAGEMENT LP
<a href="browse-edgar?action=getcompany&amp;CIK=1229262">0001229262</a>   GOLDMAN SACHS ASSET MANAGEMENT, L.P.
<a href="browse-edgar?action=getcompany&amp;CIK=1088084">0001088084</a>   GOLDMAN SACHS ASSET MANAGEMENT/
<a href="browse-edgar?action=getcompany&amp;CIK=1419270">0001419270</a>   GOLDMAN SACHS AT INVESTORS OFFSHORE LP
<a href="browse-edgar?action=getcompany&amp;CIK=1098457">0001098457</a>   GOLDMAN SACHS BANK AG
<a href="browse-edgar?action=getcompany&amp;CIK=1866894">0001866894</a>   GOLDMAN SACHS BANK EUROPE SE
<a href="browse-edgar?action=getcompany&amp;CIK=1886709">0001886709</a>   GOLDMAN SACHS BANK USA
<a href="browse-edgar?action=getcompany&amp;CIK=1572694">0001572694</a>   GOLDMAN SACHS BDC, INC.
<a href="browse-edgar?action=getcompany&amp;CIK=1173389">0001173389</a>   GOLDMAN SACHS BLOBAL RELATIVE VALUE LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1414508">0001414508</a>   GOLDMAN SACHS BMET INVESTORS LP
<a href="browse-edgar?action=getcompany&amp;CIK=1414508">0001414508</a>   GOLDMAN SACHS BMET INVESTORS LP
<a href="browse-edgar?action=getcompany&amp;CIK=1537467">0001537467</a>   GOLDMAN SACHS BMET INVESTORS OFFSHORE HOLDINGS, LP
<a href="browse-edgar?action=getcompany&amp;CIK=1414744">0001414744</a>   GOLDMAN SACHS BMET INVESTORS OFFSHORE LP
<a href="browse-edgar?action=getcompany&amp;CIK=1365054">0001365054</a>   GOLDMAN SACHS CABLE INVESTORS L P
<a href="browse-edgar?action=getcompany&amp;CIK=1277121">0001277121</a>   GOLDMAN SACHS CAPITAL I
<a href="browse-edgar?action=getcompany&amp;CIK=1277123">0001277123</a>   GOLDMAN SACHS CAPITAL II
<a href="browse-edgar?action=getcompany&amp;CIK=1277127">0001277127</a>   GOLDMAN SACHS CAPITAL II
<a href="browse-edgar?action=getcompany&amp;CIK=1277125">0001277125</a>   GOLDMAN SACHS CAPITAL III
<a href="browse-edgar?action=getcompany&amp;CIK=1318844">0001318844</a>   GOLDMAN SACHS CAPITAL III
<a href="browse-edgar?action=getcompany&amp;CIK=1277127">0001277127</a>   GOLDMAN SACHS CAPITAL IV
<a href="browse-edgar?action=getcompany&amp;CIK=1360190">0001360190</a>   GOLDMAN SACHS CAPITAL PARTNERS V 1A LP
<a href="browse-edgar?action=getcompany&amp;CIK=1359661">0001359661</a>   GOLDMAN SACHS CAPITAL PARTNERS V-1 LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1359658">0001359658</a>   GOLDMAN SACHS CAPITAL PARTNERS V-1 P L
<a href="browse-edgar?action=getcompany&amp;CIK=1318844">0001318844</a>   GOLDMAN SACHS CAPITAL V
<a href="browse-edgar?action=getcompany&amp;CIK=1318841">0001318841</a>   GOLDMAN SACHS CAPITAL VI
<a href="browse-edgar?action=getcompany&amp;CIK=1711023">0001711023</a>   GOLDMAN SACHS CAPITAL VII
<a href="browse-edgar?action=getcompany&amp;CIK=1424424">0001424424</a>   GOLDMAN SACHS CATASTROPHE RISK PREMIUM OPPORTUNITIES FUND II LP
<a href="browse-edgar?action=getcompany&amp;CIK=1387261">0001387261</a>   GOLDMAN SACHS CATASTROPHE RISK PREMIUM OPPORTUNITIES FUND LP
<a href="browse-edgar?action=getcompany&amp;CIK=1459665">0001459665</a>   GOLDMAN SACHS CATASTROPHE RISK PREMIUM OPPORTUNITIES FUND OFFSHORE III LP
<a href="browse-edgar?action=getcompany&amp;CIK=1387258">0001387258</a>   GOLDMAN SACHS CATASTROPHE RISK PREMIUM OPPORTUNITIES FUND OFFSHORE LP
<a href="browse-edgar?action=getcompany&amp;CIK=1459664">0001459664</a>   GOLDMAN SACHS CATASTROPHE RISK PREMIUM OPPORTUNITIES MASTER FUND III LP
<a href="browse-edgar?action=getcompany&amp;CIK=1361262">0001361262</a>   GOLDMAN SACHS COLUMBUS CO-INVESTMENT FUND L P
<a href="browse-edgar?action=getcompany&amp;CIK=1361263">0001361263</a>   GOLDMAN SACHS COLUMBUS CO-INVESTMENT FUND OFFSHORE L P
<a href="browse-edgar?action=getcompany&amp;CIK=1318425">0001318425</a>   GOLDMAN SACHS COMMODITIES FUND LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1318424">0001318424</a>   GOLDMAN SACHS COMMODITIES FUND OFFSHORE LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1387266">0001387266</a>   GOLDMAN SACHS COMMODITIES OPPORTUNITIES FUND OFFSHORE LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1397665">0001397665</a>   GOLDMAN SACHS COMMODITY OPPORTUNITIES FUND LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1387266">0001387266</a>   GOLDMAN SACHS COMMODITY OPPORTUNITIES FUND OFFSHORE LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1416866">0001416866</a>   GOLDMAN SACHS CONCENTRATED MEZZANINE &amp; DISTRESSED FUND II LP
<a href="browse-edgar?action=getcompany&amp;CIK=1362427">0001362427</a>   GOLDMAN SACHS CONCENTRATED MEZZANINE &amp; DISTRESSED FUND LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1474029">0001474029</a>   GOLDMAN SACHS CONVERTIBLE OPPORTUNITIES MASTER FUND, L.P.
<a href="browse-edgar?action=getcompany&amp;CIK=1410120">0001410120</a>   GOLDMAN SACHS CORE GLOBAL FLEX FUND
<a href="browse-edgar?action=getcompany&amp;CIK=1381506">0001381506</a>   GOLDMAN SACHS CORE JAPAN FLEX FUND
<a href="browse-edgar?action=getcompany&amp;CIK=1354147">0001354147</a>   GOLDMAN SACHS CORE SM EAFE FLEX FUND
<a href="browse-edgar?action=getcompany&amp;CIK=1354146">0001354146</a>   GOLDMAN SACHS CORE SM US FLEX FUND
<a href="browse-edgar?action=getcompany&amp;CIK=1354146">0001354146</a>   GOLDMAN SACHS CORE US FLEX FUND
<a href="browse-edgar?action=getcompany&amp;CIK=1461109">0001461109</a>   GOLDMAN SACHS CORPORATE CREDIT INVESTMENT FUND, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1796233">0001796233</a>   GOLDMAN SACHS CREDIT INCOME FUND
<a href="browse-edgar?action=getcompany&amp;CIK=1438026">0001438026</a>   GOLDMAN SACHS CREDIT OPPORTUNITIES 2008 FUND LP
<a href="browse-edgar?action=getcompany&amp;CIK=1438028">0001438028</a>   GOLDMAN SACHS CREDIT OPPORTUNITIES 2008 FUND OFFSHORE LP
<a href="browse-edgar?action=getcompany&amp;CIK=1232060">0001232060</a>   GOLDMAN SACHS CREDIT PARTNERS LP
<a href="browse-edgar?action=getcompany&amp;CIK=1457200">0001457200</a>   GOLDMAN SACHS CREDIT STRATEGIES FUND
<a href="browse-edgar?action=getcompany&amp;CIK=1265375">0001265375</a>   GOLDMAN SACHS CURRENCY STRATEGIES FUND LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1297480">0001297480</a>   GOLDMAN SACHS CURRENCY TRADING OPPORTUNITIES FUND PLC
<a href="browse-edgar?action=getcompany&amp;CIK=1286545">0001286545</a>   GOLDMAN SACHS CURRENCY TRANDING OPPORTUNITIES FUND LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1412549">0001412549</a>   GOLDMAN SACHS DEVELOPING MARKETS REAL ESTATE CO
<a href="browse-edgar?action=getcompany&amp;CIK=1411676">0001411676</a>   GOLDMAN SACHS DEVELOPING MARKETS REAL ESTATE PARTNERS (US) LP
<a href="browse-edgar?action=getcompany&amp;CIK=1417681">0001417681</a>   GOLDMAN SACHS DEVELOPING MARKETS REAL ESTATE PARTNERS PMD ESC FUND LP
<a href="browse-edgar?action=getcompany&amp;CIK=1417685">0001417685</a>   GOLDMAN SACHS DEVELOPING MARKETS REAL ESTATE PARTNERS PMD ESC FUND OFFSHORE LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1417680">0001417680</a>   GOLDMAN SACHS DEVELOPING MARKETS REAL ESTATE PARTNERS PMD QP FUND LP
<a href="browse-edgar?action=getcompany&amp;CIK=1417682">0001417682</a>   GOLDMAN SACHS DEVELOPING MARKETS REAL ESTATE PARTNERS QP FUND OFFSHORE LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1405653">0001405653</a>   GOLDMAN SACHS DGC INVESTORS LP
<a href="browse-edgar?action=getcompany&amp;CIK=1472038">0001472038</a>   GOLDMAN SACHS DGC INVESTORS OFFSHORE HOLDINGS, L.P.
<a href="browse-edgar?action=getcompany&amp;CIK=1232063">0001232063</a>   GOLDMAN SACHS DIRECT INVESTMENT FUND 2000 LP
<a href="browse-edgar?action=getcompany&amp;CIK=1357826">0001357826</a>   GOLDMAN SACHS DIRECT STRATEGIES 2006 FUND LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1357824">0001357824</a>   GOLDMAN SACHS DIRECT STRATEGIES 2006 FUND OFFSHORE LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1314778">0001314778</a>   GOLDMAN SACHS DIRECT STRATEGIES FUND II LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1314780">0001314780</a>   GOLDMAN SACHS DIRECT STRATEGIES FUND II OFFSHORE LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1277047">0001277047</a>   GOLDMAN SACHS DIRECT STRATEGIES FUND LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1291119">0001291119</a>   GOLDMAN SACHS DIRECT STRATEGIES FUND PLC
<a href="browse-edgar?action=getcompany&amp;CIK=1415718">0001415718</a>   GOLDMAN SACHS DIRECT STRATEGIES FUNDAMENTAL FUND LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1387264">0001387264</a>   GOLDMAN SACHS DIRECT STRATEGIES QUANTATIVE FUND OFFSHORE LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1333737">0001333737</a>   GOLDMAN SACHS DIRECT STRATEGIES QUANTITATIVE &amp; ACTIVE FUND LLC
<a href="browse-edgar?action=getcompany&amp;CIK=906352">0000906352</a>   FIRST EAGLE FUNDS INC
<a href="browse-edgar?action=getcompany&amp;CIK=1464963">0001464963</a>   FIRST EAGLE ALTERNATIVE CAPITAL BDC, INC.
<a href="browse-edgar?action=getcompany&amp;CIK=1595229">0001595229</a>   FIRST EAGLE ALTERNATIVE CAPITAL HOLDINGS, INC.
<a href="browse-edgar?action=getcompany&amp;CIK=1852781">0001852781</a>   FIRST EAGLE ALTERNATIVE CREDIT EU, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1491455">0001491455</a>   FIRST EAGLE ALTERNATIVE CREDIT, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1468266">0001468266</a>   FIRST EAGLE BANK LOAN SELECT FUND
<a href="browse-edgar?action=getcompany&amp;CIK=1468265">0001468265</a>   FIRST EAGLE BANK LOAN SELECT FUND (OFFSHORE)
<a href="browse-edgar?action=getcompany&amp;CIK=1791280">0001791280</a>   FIRST EAGLE BDC ADVISER, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1751252">0001751252</a>   FIRST EAGLE BDC, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1751518">0001751518</a>   FIRST EAGLE BERKELEY FUND CLO LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1850221">0001850221</a>   FIRST EAGLE BSL CLO 2019-1 LTD.
<a href="browse-edgar?action=getcompany&amp;CIK=1751375">0001751375</a>   FIRST EAGLE CLARENDON FUND CLO LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1751414">0001751414</a>   FIRST EAGLE COMMERCIAL LOAN FUNDING 2016-1 LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1751421">0001751421</a>   FIRST EAGLE COMMERCIAL LOAN ORIGINATOR I LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1340639">0001340639</a>   FIRST EAGLE CONTRARIAN VALUE FUND QP L P
<a href="browse-edgar?action=getcompany&amp;CIK=1340701">0001340701</a>   FIRST EAGLE CONTRARIAN VALUE OFFSHORE FUND LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1818416">0001818416</a>   FIRST EAGLE CREDIT OPPORTUNITIES FUND
<a href="browse-edgar?action=getcompany&amp;CIK=1850759">0001850759</a>   FIRST EAGLE CREDIT OPPORTUNITIES FUND SPV, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1751428">0001751428</a>   FIRST EAGLE DARTMOUTH HOLDING LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1971275">0001971275</a>   FIRST EAGLE DCF-A FUNDING, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1690369">0001690369</a>   FIRST EAGLE DIRECT LENDING CO-INVEST III (E), LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1670230">0001670230</a>   FIRST EAGLE DIRECT LENDING CO-INVEST III, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1731962">0001731962</a>   FIRST EAGLE DIRECT LENDING FUND I (EE), LP
<a href="browse-edgar?action=getcompany&amp;CIK=1725776">0001725776</a>   FIRST EAGLE DIRECT LENDING FUND I (PARALLEL), LP
<a href="browse-edgar?action=getcompany&amp;CIK=1725775">0001725775</a>   FIRST EAGLE DIRECT LENDING FUND I, LP
<a href="browse-edgar?action=getcompany&amp;CIK=1670357">0001670357</a>   FIRST EAGLE DIRECT LENDING FUND III (A), LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1633245">0001633245</a>   FIRST EAGLE DIRECT LENDING FUND III, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1747760">0001747760</a>   FIRST EAGLE DIRECT LENDING FUND IV, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1747763">0001747763</a>   FIRST EAGLE DIRECT LENDING IV CO-INVEST, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1813462">0001813462</a>   FIRST EAGLE DIRECT LENDING LEVERED FUND IV SPV, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1747759">0001747759</a>   FIRST EAGLE DIRECT LENDING LEVERED FUND IV, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1854121">0001854121</a>   FIRST EAGLE DIRECT LENDING V-A (BLOCKED), LP
<a href="browse-edgar?action=getcompany&amp;CIK=1849941">0001849941</a>   FIRST EAGLE DIRECT LENDING V-A, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1854119">0001854119</a>   FIRST EAGLE DIRECT LENDING V-B (BLOCKED), LP
<a href="browse-edgar?action=getcompany&amp;CIK=1919886">0001919886</a>   FIRST EAGLE DIRECT LENDING V-B SPV, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1849945">0001849945</a>   FIRST EAGLE DIRECT LENDING V-B, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1854242">0001854242</a>   FIRST EAGLE DIRECT LENDING V-C (OFFSHORE), SCSP
<a href="browse-edgar?action=getcompany&amp;CIK=1849954">0001849954</a>   FIRST EAGLE DIRECT LENDING V-C SCSP
<a href="browse-edgar?action=getcompany&amp;CIK=1751147">0001751147</a>   FIRST EAGLE DL FUND I AGGREGATOR LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1859468">0001859468</a>   FIRST EAGLE DL V-A FUNDING, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1481769">0001481769</a>   FIRST EAGLE FUND N.V.
<a href="browse-edgar?action=getcompany&amp;CIK=807986">0000807986</a>   FIRST EAGLE FUND OF AMERICA INC
<a href="browse-edgar?action=getcompany&amp;CIK=807986">0000807986</a>   FIRST EAGLE FUNDS   
<a href="browse-edgar?action=getcompany&amp;CIK=906352">0000906352</a>   FIRST EAGLE FUNDS   
<a href="browse-edgar?action=getcompany&amp;CIK=1814535">0001814535</a>   FIRST EAGLE GLOBAL EQUITY FUND, LP
<a href="browse-edgar?action=getcompany&amp;CIK=1876160">0001876160</a>   FIRST EAGLE GLOBAL OPPORTUNITIES FUND
<a href="browse-edgar?action=getcompany&amp;CIK=1484313">0001484313</a>   FIRST EAGLE GLOBAL VALUE FUND, LP
<a href="browse-edgar?action=getcompany&amp;CIK=1459713">0001459713</a>   FIRST EAGLE GOODHOPE INTERNATIONAL LTD.
<a href="browse-edgar?action=getcompany&amp;CIK=1459689">0001459689</a>   FIRST EAGLE GOODHOPE PARTNERS L.P.
<a href="browse-edgar?action=getcompany&amp;CIK=1601749">0001601749</a>   FIRST EAGLE HIGH YIELD FUND, LP
<a href="browse-edgar?action=getcompany&amp;CIK=1637141">0001637141</a>   FIRST EAGLE HOLDINGS, INC.
<a href="browse-edgar?action=getcompany&amp;CIK=1459976">0001459976</a>   FIRST EAGLE INSTITUTIONAL FUNDS LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1850033">0001850033</a>   FIRST EAGLE INSTITUTIONAL GOLD FUND, LP
<a href="browse-edgar?action=getcompany&amp;CIK=1814519">0001814519</a>   FIRST EAGLE INTERNATIONAL EQUITY FUND, LP
<a href="browse-edgar?action=getcompany&amp;CIK=913622">0000913622</a>   FIRST EAGLE INTERNATIONAL FUND INC
<a href="browse-edgar?action=getcompany&amp;CIK=1634065">0001634065</a>   FIRST EAGLE INTERNATIONAL SMALL CAP VALUE FUND LP
<a href="browse-edgar?action=getcompany&amp;CIK=1450194">0001450194</a>   FIRST EAGLE INTERNATIONAL VALUE FUND, LP
<a href="browse-edgar?action=getcompany&amp;CIK=1325447">0001325447</a>   FIRST EAGLE INVESTMENT MANAGEMENT, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1814818">0001814818</a>   FIRST EAGLE MMDL WH I LTD.
<a href="browse-edgar?action=getcompany&amp;CIK=1583978">0001583978</a>   FIRST EAGLE MULTI-ASSET ABSOLUTE RETURN FUND (QP), LP
<a href="browse-edgar?action=getcompany&amp;CIK=2018765">0002018765</a>   FIRST EAGLE MUNICIPAL HIGH INCOME FUND
<a href="browse-edgar?action=getcompany&amp;CIK=1857170">0001857170</a>   FIRST EAGLE OPPORTUNITY FUND LP
<a href="browse-edgar?action=getcompany&amp;CIK=1000249">0001000249</a>   FIRST EAGLE OVERSEAS VARIABLE FUND
<a href="browse-edgar?action=getcompany&amp;CIK=1459660">0001459660</a>   FIRST EAGLE PACIFIC FUND LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1459660">0001459660</a>   FIRST EAGLE PACIFIC FUND LTD.
<a href="browse-edgar?action=getcompany&amp;CIK=1506963">0001506963</a>   FIRST EAGLE PACIFIC FUND, LP
<a href="browse-edgar?action=getcompany&amp;CIK=1751376">0001751376</a>   FIRST EAGLE PRIVATE CREDIT ADVISORS, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1890107">0001890107</a>   FIRST EAGLE PRIVATE CREDIT FUND
<a href="browse-edgar?action=getcompany&amp;CIK=1373561">0001373561</a>   FIRST EAGLE PRIVATE CREDIT, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=2006189">0002006189</a>   FIRST EAGLE REAL ESTATE DEBT FUND
<a href="browse-edgar?action=getcompany&amp;CIK=2006189">0002006189</a>   FIRST EAGLE REAL ESTATE LENDING FUND
<a href="browse-edgar?action=getcompany&amp;CIK=1583001">0001583001</a>   FIRST EAGLE SENIOR LOAN FUND
<a href="browse-edgar?action=getcompany&amp;CIK=1791280">0001791280</a>   FIRST EAGLE SEPARATE ACCOUNT MANAGEMENT, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=906352">0000906352</a>   FIRST EAGLE SOGEN FUNDS INC
<a href="browse-edgar?action=getcompany&amp;CIK=1000249">0001000249</a>   FIRST EAGLE SOGEN OVERSEAS VARIABLE FUND
<a href="browse-edgar?action=getcompany&amp;CIK=1747701">0001747701</a>   FIRST EAGLE STRATEGIC FUNDING. LLC
<a href="browse-edgar?action=getcompany&amp;CIK=2050541">0002050541</a>   FIRST EAGLE TACTICAL MUNICIPAL OPPORTUNITIES FUND
<a href="browse-edgar?action=getcompany&amp;CIK=1583989">0001583989</a>   FIRST EAGLE TAIL HEDGE FUND (QP), LP
<a href="browse-edgar?action=getcompany&amp;CIK=807986">0000807986</a>   FIRST EAGLE TRUST   
<a href="browse-edgar?action=getcompany&amp;CIK=1857170">0001857170</a>   FIRST EAGLE US SMALL CAP OPPORTUNITY FUND LP
<a href="browse-edgar?action=getcompany&amp;CIK=1481559">0001481559</a>   FIRST EAGLE VALUE IN BIOTECHNOLOGY FUND (QP), LP
<a href="browse-edgar?action=getcompany&amp;CIK=1457518">0001457518</a>   FIRST EAGLE VALUE IN BIOTECHNOLOGY MASTER FUND, LTD.
<a href="browse-edgar?action=getcompany&amp;CIK=1340784">0001340784</a>   FIRST EAGLE VALUE IN BIOTECHNOLOGY OFFSHORE FUND LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1459980">0001459980</a>   FIRST EAGLE VALUE REALIZATION FUND LP
<a href="browse-edgar?action=getcompany&amp;CIK=1459978">0001459978</a>   FIRST EAGLE VALUE REALIZATION FUND LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1000249">0001000249</a>   FIRST EAGLE VARIABLE FUNDS
<a href="browse-edgar?action=getcompany&amp;CIK=1751450">0001751450</a>   FIRST EAGLE WAREHOUSE FUNDING I LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1647749">0001647749</a>   FIRST EAGLE WORLD OPPORTUNITIES FUND LP
<a href="browse-edgar?action=getcompany&amp;CIK=1374733">0001374733</a>   FIRST EAGLE WORLDWIDE SELECT FUND L P
<a href="browse-edgar?action=getcompany&amp;CIK=1412446">0001412446</a>   FIRST EAGLE WORLDWIDE SELECT FUND LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1581500">0001581500</a>   KOPERNIK GLOBAL ALL-CAP FUND, LP
<a href="browse-edgar?action=getcompany&amp;CIK=1581505">0001581505</a>   KOPERNIK GLOBAL ALL-CAP OFFSHORE FUND, LTD.
<a href="browse-edgar?action=getcompany&amp;CIK=1599814">0001599814</a>   KOPERNIK GLOBAL INVESTORS, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1581504">0001581504</a>   KOPERNIK GLOBAL LONG-TERM OPPORTUNITIES FUND, LP
<a href="browse-edgar?action=getcompany&amp;CIK=1942894">0001942894</a>   KOPERNIK GLOBAL LONG-TERM OPPORTUNITIES FUND, LP/GUERNSEY
<a href="browse-edgar?action=getcompany&amp;CIK=1941588">0001941588</a>   KOPERNIK GLOBAL LONG-TERM OPPORTUNITIES FUND, LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1581504">0001581504</a>   KOPERNIK GLOBAL REAL ASSET FUND, LP
<a href="browse-edgar?action=getcompany&amp;CIK=1581501">0001581501</a>   KOPERNIK GLOBAL UNCONSTRAINED FUND, LP
<a href="browse-edgar?action=getcompany&amp;CIK=1586561">0001586561</a>   KOPERNIK GLOBAL UNCONSTRAINED OFFSHORE FUND, LTD.
<a href="browse-edgar?action=getcompany&amp;CIK=938744">0000938744</a>   SCHWAB ADVANTAGE TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=1061698">0001061698</a>   SCHWAB ALTERITY, L.P.
<a href="browse-edgar?action=getcompany&amp;CIK=1137090">0001137090</a>   SCHWAB ANDREW       
<a href="browse-edgar?action=getcompany&amp;CIK=1598549">0001598549</a>   SCHWAB ANDREW J.    
<a href="browse-edgar?action=getcompany&amp;CIK=918266">0000918266</a>   SCHWAB ANNUITY PORTFOLIOS
<a href="browse-edgar?action=getcompany&amp;CIK=1133528">0001133528</a>   SCHWAB CAPITAL MARKETS L P
<a href="browse-edgar?action=getcompany&amp;CIK=63461">0000063461</a>   SCHWAB CAPITAL MARKETS L.P.
<a href="browse-edgar?action=getcompany&amp;CIK=904333">0000904333</a>   SCHWAB CAPITAL TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=1287972">0001287972</a>   SCHWAB CAPITAL TRUST I
<a href="browse-edgar?action=getcompany&amp;CIK=1287973">0001287973</a>   SCHWAB CAPITAL TRUST II
<a href="browse-edgar?action=getcompany&amp;CIK=1287974">0001287974</a>   SCHWAB CAPITAL TRUST III
<a href="browse-edgar?action=getcompany&amp;CIK=1535839">0001535839</a>   SCHWAB CHARITABLE FUND
<a href="browse-edgar?action=getcompany&amp;CIK=751448">0000751448</a>   SCHWAB CHARLES &amp; CO INC /TA
<a href="browse-edgar?action=getcompany&amp;CIK=316709">0000316709</a>   SCHWAB CHARLES CORP 
<a href="browse-edgar?action=getcompany&amp;CIK=857156">0000857156</a>   SCHWAB CHARLES FAMILY OF FUNDS
<a href="browse-edgar?action=getcompany&amp;CIK=884546">0000884546</a>   SCHWAB CHARLES INVESTMENT MANAGEMENT INC
<a href="browse-edgar?action=getcompany&amp;CIK=1125972">0001125972</a>   SCHWAB CHARLES JR   
<a href="browse-edgar?action=getcompany&amp;CIK=923738">0000923738</a>   SCHWAB CHARLES R    
<a href="browse-edgar?action=getcompany&amp;CIK=923738">0000923738</a>   SCHWAB CHARLES R.   
<a href="browse-edgar?action=getcompany&amp;CIK=1032626">0001032626</a>   SCHWAB DAVID C      
<a href="browse-edgar?action=getcompany&amp;CIK=1014049">0001014049</a>   SCHWAB DAVID E II   
<a href="browse-edgar?action=getcompany&amp;CIK=1561505">0001561505</a>   SCHWAB DAVID M      
<a href="browse-edgar?action=getcompany&amp;CIK=1231506">0001231506</a>   SCHWAB FREDERICK J  
<a href="browse-edgar?action=getcompany&amp;CIK=1792085">0001792085</a>   SCHWAB GARY S.      
<a href="browse-edgar?action=getcompany&amp;CIK=1213140">0001213140</a>   SCHWAB GISELA       
<a href="browse-edgar?action=getcompany&amp;CIK=1213140">0001213140</a>   SCHWAB GISELA MD    
<a href="browse-edgar?action=getcompany&amp;CIK=1553272">0001553272</a>   SCHWAB HOLGER       
<a href="browse-edgar?action=getcompany&amp;CIK=1014049">0001014049</a>   SCHWAB II DAVID E   
<a href="browse-edgar?action=getcompany&amp;CIK=869365">0000869365</a>   SCHWAB INVESTMENTS  
<a href="browse-edgar?action=getcompany&amp;CIK=1232486">0001232486</a>   SCHWAB JOHN D       
<a href="browse-edgar?action=getcompany&amp;CIK=1198548">0001198548</a>   SCHWAB JOHN N       
<a href="browse-edgar?action=getcompany&amp;CIK=1249289">0001249289</a>   SCHWAB JOHN R       
<a href="browse-edgar?action=getcompany&amp;CIK=1226581">0001226581</a>   SCHWAB LOWELL F     
<a href="browse-edgar?action=getcompany&amp;CIK=1839606">0001839606</a>   SCHWAB MARCY        
<a href="browse-edgar?action=getcompany&amp;CIK=1699816">0001699816</a>   SCHWAB MARK J.      
<a href="browse-edgar?action=getcompany&amp;CIK=1215405">0001215405</a>   SCHWAB NELSON III   
<a href="browse-edgar?action=getcompany&amp;CIK=1178475">0001178475</a>   SCHWAB OIL &amp; GAS LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1561543">0001561543</a>   SCHWAB PETER E      
<a href="browse-edgar?action=getcompany&amp;CIK=1297343">0001297343</a>   SCHWAB RETIREMENT PLAN SERVICES INC
<a href="browse-edgar?action=getcompany&amp;CIK=1005437">0001005437</a>   SCHWAB RETIREMENT PLAN SERVICES INC /TA
<a href="browse-edgar?action=getcompany&amp;CIK=1305835">0001305835</a>   SCHWAB RETIREMENT PLAN SERVICES, INC.
<a href="browse-edgar?action=getcompany&amp;CIK=1581861">0001581861</a>   SCHWAB RICHARD J    
<a href="browse-edgar?action=getcompany&amp;CIK=1496106">0001496106</a>   SCHWAB ROBERT       
<a href="browse-edgar?action=getcompany&amp;CIK=1837414">0001837414</a>   SCHWAB STEVEN ANTHONY
<a href="browse-edgar?action=getcompany&amp;CIK=1042252">0001042252</a>   SCHWAB STRATEGIC TEN TRUST 1997 SERIES A
<a href="browse-edgar?action=getcompany&amp;CIK=1454889">0001454889</a>   SCHWAB STRATEGIC TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=1454889">0001454889</a>   SCHWAB STRATEGIC TRUST
<a href="browse-edgar?action=getcompany&amp;CIK=1202958">0001202958</a>   SCHWAB SUSAN C      
<a href="browse-edgar?action=getcompany&amp;CIK=1065071">0001065071</a>   SCHWAB TRUSTS       
<a href="browse-edgar?action=getcompany&amp;CIK=1053262">0001053262</a>   SCHWAB TRUSTS SCHWAB TEN TRUST 1998 SERIES A
<a href="browse-edgar?action=getcompany&amp;CIK=1062542">0001062542</a>   SCHWAB TRUSTS SCHWAB TEN TRUST 1998 SERIES B
<a href="browse-edgar?action=getcompany&amp;CIK=1070948">0001070948</a>   SCHWAB TRUSTS SCHWAB TEN TRUST 1998 SERIES C
<a href="browse-edgar?action=getcompany&amp;CIK=1080303">0001080303</a>   SCHWAB TRUSTS SCHWAB TEN TRUST 1999 SERIES A
<a href="browse-edgar?action=getcompany&amp;CIK=1089342">0001089342</a>   SCHWAB TRUSTS SCHWAB TEN TRUST 1999 SERIES B
<a href="browse-edgar?action=getcompany&amp;CIK=1100464">0001100464</a>   SCHWAB TRUSTS SCHWAB TEN TRUST 2000 SERIES A
<a href="browse-edgar?action=getcompany&amp;CIK=1111245">0001111245</a>   SCHWAB TRUSTS SCHWAB TEN TRUST 2000 SERIES B
<a href="browse-edgar?action=getcompany&amp;CIK=1121906">0001121906</a>   SCHWAB TRUSTS SCHWAB TEN TRUST 2000 SERIES C
<a href="browse-edgar?action=getcompany&amp;CIK=1129864">0001129864</a>   SCHWAB TRUSTS SCHWAB TEN TRUST 2001 SERIES A
<a href="browse-edgar?action=getcompany&amp;CIK=1157609">0001157609</a>   SCHWAB TRUSTS SCHWAB TEN TRUST 2001 SERIES C
<a href="browse-edgar?action=getcompany&amp;CIK=1164389">0001164389</a>   SCHWAB TRUSTS SCHWAB TEN TRUST 2002 SERIES A
<a href="browse-edgar?action=getcompany&amp;CIK=1172630">0001172630</a>   SCHWAB TRUSTS SCHWAB TEN TRUST 2002 SERIES B
<a href="browse-edgar?action=getcompany&amp;CIK=1191142">0001191142</a>   SCHWAB TRUSTS SCHWAB TEN TRUST 2002 SERIES C
<a href="browse-edgar?action=getcompany&amp;CIK=1249680">0001249680</a>   SCHWAB TRUSTS SCHWAB TEN TRUST 2003 SEREIS B
<a href="browse-edgar?action=getcompany&amp;CIK=1221457">0001221457</a>   SCHWAB TRUSTS SCHWAB TEN TRUST 2003 SERIES A
<a href="browse-edgar?action=getcompany&amp;CIK=1249680">0001249680</a>   SCHWAB TRUSTS SCHWAB TEN TRUST 2003 SERIES B
<a href="browse-edgar?action=getcompany&amp;CIK=1270759">0001270759</a>   SCHWAB TRUSTS SCHWAB TEN TRUST 2003 SERIES C
<a href="browse-edgar?action=getcompany&amp;CIK=1284718">0001284718</a>   SCHWAB TRUSTS SCHWAB TEN TRUST 2004 SERIES A
<a href="browse-edgar?action=getcompany&amp;CIK=1287749">0001287749</a>   SCHWAB TRUSTS SCHWAB TEN TRUST 2004 SERIES B
<a href="browse-edgar?action=getcompany&amp;CIK=1139232">0001139232</a>   SCHWAB TRUSTS SCHWAB TEN TRUSTS 2001 SERIES B
<a href="browse-edgar?action=getcompany&amp;CIK=1311244">0001311244</a>   SCHWAB TRUSTS, SCHWAB TEN TRUST, 2005 SERIES A
<a href="browse-edgar?action=getcompany&amp;CIK=1323408">0001323408</a>   SCHWAB TRUSTS, SCHWAB TEN TRUST, 2005 SERIES B
<a href="browse-edgar?action=getcompany&amp;CIK=1950787">0001950787</a>   SCHWAB-POMERANTZ CAROLYN
<a href="browse-edgar?action=getcompany&amp;CIK=1549728">0001549728</a>   SCHWABE CHARLES E.  
<a href="browse-edgar?action=getcompany&amp;CIK=1557657">0001557657</a>   SCHWABE STEFAN K.F. 
<a href="browse-edgar?action=getcompany&amp;CIK=1641001">0001641001</a>   SCHWABENKAPITAL GMBH
<a href="browse-edgar?action=getcompany&amp;CIK=1281348">0001281348</a>   SCHWABERO MARK D    
<a href="browse-edgar?action=getcompany&amp;CIK=2023175">0002023175</a>   SCHWABISH MARC
<a href="browse-edgar?action=getcompany&amp;CIK=1359190">0001359190</a>   ARTISAN: ALPHA (NON-US EQUITY) OFFSHORE LP
<a href="browse-edgar?action=getcompany&amp;CIK=1359190">0001359190</a>   ARTISAN: ALPHA PLUS SM (NON-US EQUITY) OFFSHORE LP
<a href="browse-edgar?action=getcompany&amp;CIK=1359190">0001359190</a>   ARTISAN: DYNAMIC EQUITY (NON-US EQUITY) OFFSHORE LP
<a href="browse-edgar?action=getcompany&amp;CIK=1519501">0001519501</a>   ARTISAN: DYNAMIC EQUITY (GLOBAL EQUITY) LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1557554">0001557554</a>   ARTISAN: DYNAMIC EQUITY (GLOBAL EQUITY) OFFSHORE L.P.
<a href="browse-edgar?action=getcompany&amp;CIK=1844840">0001844840</a>   ARTISAN ACQUISITION CORP.
<a href="browse-edgar?action=getcompany&amp;CIK=1512273">0001512273</a>   ARTISAN BOOKS &amp; BINDERY
<a href="browse-edgar?action=getcompany&amp;CIK=1844896">0001844896</a>   ARTISAN CHINA POST-VENTURE FUND LP
<a href="browse-edgar?action=getcompany&amp;CIK=1844903">0001844903</a>   ARTISAN CHINA POST-VENTURE OFFSHORE FUND LP
<a href="browse-edgar?action=getcompany&amp;CIK=1971126">0001971126</a>   ARTISAN CO-INVEST SCSP
<a href="browse-edgar?action=getcompany&amp;CIK=1048982">0001048982</a>   ARTISAN COMPONENTS INC
<a href="browse-edgar?action=getcompany&amp;CIK=1530425">0001530425</a>   ARTISAN CONSUMER GOODS, INC.
<a href="browse-edgar?action=getcompany&amp;CIK=1707601">0001707601</a>   ARTISAN CREDIT OPPORTUNITIES FUND LP
<a href="browse-edgar?action=getcompany&amp;CIK=1709638">0001709638</a>   ARTISAN CREDIT OPPORTUNITIES GP LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1707599">0001707599</a>   ARTISAN CREDIT OPPORTUNITIES OFFSHORE FUND LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1656641">0001656641</a>   ARTISAN DATA, INC.  
<a href="browse-edgar?action=getcompany&amp;CIK=1791885">0001791885</a>   ARTISAN DESIGN GROUP HOLDINGS, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1762595">0001762595</a>   ARTISAN DESIGN GROUP INVESTMENTS, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1996985">0001996985</a>   ARTISAN DISLOCATION OPPORTUNITIES FUND LP
<a href="browse-edgar?action=getcompany&amp;CIK=1999614">0001999614</a>   ARTISAN DISLOCATION OPPORTUNITIES GP LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1996923">0001996923</a>   ARTISAN DISLOCATION OPPORTUNITIES OFFSHORE FUND LP
<a href="browse-edgar?action=getcompany&amp;CIK=1062521">0001062521</a>   ARTISAN DISTRIBUTORS LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1062521">0001062521</a>   ARTISAN DISTRIBUTORS LLC /BD
<a href="browse-edgar?action=getcompany&amp;CIK=1707799">0001707799</a>   ARTISAN ELKHART LLC 
<a href="browse-edgar?action=getcompany&amp;CIK=1982697">0001982697</a>   ARTISAN EMERGING MARKETS LOCAL OPPORTUNITIES FUND LP
<a href="browse-edgar?action=getcompany&amp;CIK=1095558">0001095558</a>   ARTISAN ENTERTAINMENT INC
<a href="browse-edgar?action=getcompany&amp;CIK=1093201">0001093201</a>   ARTISAN EQUITY LTD  
<a href="browse-edgar?action=getcompany&amp;CIK=1551380">0001551380</a>   ARTISAN FIXED INCOME FUND, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1824032">0001824032</a>   ARTISAN FOCUS DYNAMIC EQUITY SELECT LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1840531">0001840531</a>   ARTISAN FOCUS DYNAMIC EQUITY SELECT LTD
<a href="browse-edgar?action=getcompany&amp;CIK=2058387">0002058387</a>   ARTISAN FRANCHISE FUND LP
<a href="browse-edgar?action=getcompany&amp;CIK=2058429">0002058429</a>   ARTISAN FRANCHISE OFFSHORE FUND LP
<a href="browse-edgar?action=getcompany&amp;CIK=935015">0000935015</a>   ARTISAN FUNDS INC   
<a href="browse-edgar?action=getcompany&amp;CIK=1936529">0001936529</a>   ARTISAN GLOBAL OPPORTUNITIES FUND LP
<a href="browse-edgar?action=getcompany&amp;CIK=2042472">0002042472</a>   ARTISAN GLOBAL SPECIAL SITUATIONS FUND LP
<a href="browse-edgar?action=getcompany&amp;CIK=2042439">0002042439</a>   ARTISAN GLOBAL SPECIAL SITUATIONS GP LLC
<a href="browse-edgar?action=getcompany&amp;CIK=2042464">0002042464</a>   ARTISAN GLOBAL SPECIAL SITUATIONS OFFSHORE FUND LP
<a href="browse-edgar?action=getcompany&amp;CIK=1823960">0001823960</a>   ARTISAN INTERNATIONAL EXPLORER FUND LP
<a href="browse-edgar?action=getcompany&amp;CIK=1167755">0001167755</a>   ARTISAN INTERNATIONAL LONG SHORT FUND LIMITED PARTNERSHIP
<a href="browse-edgar?action=getcompany&amp;CIK=1823960">0001823960</a>   ARTISAN INTERNATIONAL SMALL CAP VALUE FUND LP
<a href="browse-edgar?action=getcompany&amp;CIK=1086156">0001086156</a>   ARTISAN INVESTMENT CORP
<a href="browse-edgar?action=getcompany&amp;CIK=1466152">0001466152</a>   ARTISAN INVESTMENTS GP LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1844839">0001844839</a>   ARTISAN LLC         
<a href="browse-edgar?action=getcompany&amp;CIK=1994003">0001994003</a>   ARTISAN MADE, LLC   
<a href="browse-edgar?action=getcompany&amp;CIK=2044662">0002044662</a>   ARTISAN MAKER HOLDINGS, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=2044932">0002044932</a>   ARTISAN MAKER SPLITTER, LP
<a href="browse-edgar?action=getcompany&amp;CIK=1976571">0001976571</a>   ARTISAN MCFARLIN CAPITAL, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1587101">0001587101</a>   ARTISAN MOBILE, INC.
<a href="browse-edgar?action=getcompany&amp;CIK=1654673">0001654673</a>   ARTISAN NORTH, LLC  
<a href="browse-edgar?action=getcompany&amp;CIK=1581413">0001581413</a>   ARTISAN ON 18TH VENTURE, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1517302">0001517302</a>   ARTISAN PARTNERS ASSET MANAGEMENT INC.
<a href="browse-edgar?action=getcompany&amp;CIK=1062521">0001062521</a>   ARTISAN PARTNERS DISTRIBUTORS LLC
<a href="browse-edgar?action=getcompany&amp;CIK=935015">0000935015</a>   ARTISAN PARTNERS FUNDS INC
<a href="browse-edgar?action=getcompany&amp;CIK=1010643">0001010643</a>   ARTISAN PARTNERS HOLDINGS LP
<a href="browse-edgar?action=getcompany&amp;CIK=1466153">0001466153</a>   ARTISAN PARTNERS LIMITED PARTNERSHIP
<a href="browse-edgar?action=getcompany&amp;CIK=1010643">0001010643</a>   ARTISAN PARTNERS LTD PARTNERSHIP
<a href="browse-edgar?action=getcompany&amp;CIK=1373033">0001373033</a>   ARTISAN PHARMA, INC.
<a href="browse-edgar?action=getcompany&amp;CIK=1804740">0001804740</a>   ARTISAN PIZZA PIES OF STILLWATER, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1952832">0001952832</a>   ARTISAN PRIME 2122 WEST BUTLER, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1381598">0001381598</a>   ARTISAN SPECIAL EQUITY FUND L P
<a href="browse-edgar?action=getcompany&amp;CIK=1784552">0001784552</a>   ARTISAN SUSTAINABLE EMERGING MARKETS FUND LP
<a href="browse-edgar?action=getcompany&amp;CIK=1718741">0001718741</a>   ARTISAN THEMATIC FUND LP
<a href="browse-edgar?action=getcompany&amp;CIK=1718590">0001718590</a>   ARTISAN THEMATIC OFFSHORE FUND LTD
<a href="browse-edgar?action=getcompany&amp;CIK=1373033">0001373033</a>   ARTISAN THERAPEUTICS INC
<a href="browse-edgar?action=getcompany&amp;CIK=1975313">0001975313</a>   ARTISAN TOPCO LTD   
<a href="browse-edgar?action=getcompany&amp;CIK=1144418">0001144418</a>   ARTISAN UK PLC      
<a href="browse-edgar?action=getcompany&amp;CIK=1755424">0001755424</a>   ARTISAN'S CELLAR, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1716701">0001716701</a>   ARTISANAL BLUE NORTHERN FOODS, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=945634">0000945634</a>   ARTISANAL BRANDS, INC.
<a href="browse-edgar?action=getcompany&amp;CIK=1910506">0001910506</a>   ARTISANAL CAVES LLC 
<a href="browse-edgar?action=getcompany&amp;CIK=1850249">0001850249</a>   ARTISANAL DISTILLATES LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1861598">0001861598</a>   ARTISANAL VENTURES I, L.P.
<a href="browse-edgar?action=getcompany&amp;CIK=1644255">0001644255</a>   ARTISANAL VILLA MANAGEMENT, LLC
<a href="browse-edgar?action=getcompany&amp;CIK=1103878">0001103878</a>   ARTISANS INSURANCE LTD'''

ciks = []
for line in io.StringIO(html):
    start_of_cik = line.index('CIK=') + 4
    end_of_cik = line.find('"', start_of_cik)
    ciks.append(line[start_of_cik:end_of_cik].rjust(10, '0'))
print(ciks)

prev_length = len(ciks)
ciks = set(ciks)
new_length = len(ciks)

print(f'Duplicates deleted: {prev_length - new_length}')
for i, cik in enumerate(ciks):
    print(f'(\'{cik}\'){';' if i == len(ciks) - 1 else ','}')
