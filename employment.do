*1 MPC
import excel "C:\Users\bryennt\Desktop\filled_income.xlsx",firstrow clear
tsset year
reg C Y
est store m00

dfuller C
dfuller Y

gen dC = D.C
gen dY = D.Y

dfuller dC
dfuller dY

reg dC dY
est store m01

gen lndC = ln(dC)
gen lndY = ln(dY)

dfuller lndC
dfuller lndY

*2 labor force
import excel "C:\Users\bryennt\Desktop\wage_by_sector_filled.xlsx",firstrow clear
**2.1 trans
***OLS
gen ln_trans_wage = ln(trans_wage)
gen ln_unemploymentrate =ln(unemploymentrate)
reg trans ln_trans_wage ln_unemploymentrate 
est store m212

***IV-test
tsset year
gen Lwage_ln_trans_wage = L.ln_trans_wage
ivregress 2sls trans (ln_trans_wage = Lwage_ln_trans_wage) unemploymentrate
est store m223

*hausman
hausman m212 m223

**2.2 accom
***OLS
gen ln_accom_wage = ln(accom_wage)
reg accom ln_accom_wage ln_unemploymentrate
est store m231

***IV-test
tsset year
gen Lwage_ln_accom_wage = L.ln_accom_wage
ivregress 2sls trans (ln_accom_wage = Lwage_ln_accom_wage) ln_unemploymentrate
est store m241
*hausman
hausman m231 m241

local mm "m00 m01 m212 m223 m231 m241" 
esttab `mm' using "employment.rtf", ///
mtitle(`mm') se b(%6.4f) s(N r2) compress nogaps /// 
star(* 0.1 ** 0.05 *** 0.01) replace