## DAX Expresssion used to rank providers using qualilty measures slicers

```powerbi

Rank_HHCA = 
VAR SortOrder = SELECTEDVALUE(Quality_Measures_Sort[Name])
VAR SortMeasure = SELECTEDVALUE(HHA_Sort_By[Measures])

RETURN
IF(
    ISBLANK(SortOrder) || ISBLANK(SortMeasure),
    BLANK(),
    IF(
        SortOrder = "ASC",
    
    SWITCH(
        SELECTEDVALUE(HHA_Sort_By[Measures]),
        "Bathing Improvement Rate", RANKX(ALLSELECTED(HHA), CALCULATE(SELECTEDVALUE(HHA[Bathing_Improvement_Rate])), , ASC, DENSE),
        "Bed Mobility Rate", RANKX(ALLSELECTED(HHA), CALCULATE(SELECTEDVALUE(HHA[Bed_Mobility_Rate])), , ASC, DENSE),
        "Breathing Improvement Rate", RANKX(ALLSELECTED(HHA), CALCULATE(SELECTEDVALUE(HHA[Breathing_Improvement_Rate])), , ASC, DENSE),
        "Discharge Score", RANKX(ALLSELECTED(HHA), CALCULATE(SELECTEDVALUE(HHA[Discharge_Score])), , ASC, DENSE),
        "Drug Adherence Rate", RANKX(ALLSELECTED(HHA), CALCULATE(SELECTEDVALUE(HHA[Drug_Adherence_Rate])), , ASC, DENSE),
        "DTC Observerd Rate", RANKX(ALLSELECTED(HHA), CALCULATE(SELECTEDVALUE(HHA[DTC_Observed_Rate])), , ASC, DENSE),
        "Fall injury Rate", RANKX(ALLSELECTED(HHA), CALCULATE(SELECTEDVALUE(HHA[Fall_injury_Rate])), , ASC, DENSE),
        "Flu Shot Rate", RANKX(ALLSELECTED(HHA), CALCULATE(SELECTEDVALUE(HHA[Flu_Shot_Rate])), , ASC, DENSE),
        "Info Transfer to Patient", RANKX(ALLSELECTED(HHA), CALCULATE(SELECTEDVALUE(HHA[Info_Transfer_to_Patient])), , ASC, DENSE),
        "Info Transfer to Provider", RANKX(ALLSELECTED(HHA), CALCULATE(SELECTEDVALUE(HHA[Info_Transfer_to_Provider])), , ASC, DENSE),
        "Patient Care Star Rating", RANKX(ALLSELECTED(HHA), CALCULATE(SELECTEDVALUE(HHA[Patient_Care_Star_Rating])), , ASC, DENSE),
        "PPH Observed Rate", RANKX(ALLSELECTED(HHA), CALCULATE(SELECTEDVALUE(HHA[PPH_Observed_Rate])), , ASC, DENSE),
        "PPR Observed Rate", RANKX(ALLSELECTED(HHA), CALCULATE(SELECTEDVALUE(HHA[PPR_Observed_Rate])), , ASC, DENSE),
        "Skin Integrity Change", RANKX(ALLSELECTED(HHA), CALCULATE(SELECTEDVALUE(HHA[Skin_Integrity_Change])), , ASC, DENSE),
        "Timely Care Start Rate", RANKX(ALLSELECTED(HHA), CALCULATE(SELECTEDVALUE(HHA[Timely_Care_Start_Rate])), , ASC, DENSE),
        "Timely Med Action Rate", RANKX(ALLSELECTED(HHA), CALCULATE(SELECTEDVALUE(HHA[Timely_Med_Action_Rate])), , ASC, DENSE),
        "Walking Improvement Rate", RANKX(ALLSELECTED(HHA), CALCULATE(SELECTEDVALUE(HHA[Walking_Improvement_Rate])), , ASC, DENSE)
    ),

    SWITCH(
        SELECTEDVALUE(HHA_Sort_By[Measures]),
        "Bathing Improvement Rate", RANKX(ALLSELECTED(HHA), CALCULATE(SELECTEDVALUE(HHA[Bathing_Improvement_Rate])), , DESC, DENSE),
        "Bed Mobility Rate", RANKX(ALLSELECTED(HHA), CALCULATE(SELECTEDVALUE(HHA[Bed_Mobility_Rate])), , DESC, DENSE),
        "Breathing Improvement Rate", RANKX(ALLSELECTED(HHA), CALCULATE(SELECTEDVALUE(HHA[Breathing_Improvement_Rate])), , DESC, DENSE),
        "Discharge Score", RANKX(ALLSELECTED(HHA), CALCULATE(SELECTEDVALUE(HHA[Discharge_Score])), , DESC, DENSE),
        "Drug Adherence Rate", RANKX(ALLSELECTED(HHA), CALCULATE(SELECTEDVALUE(HHA[Drug_Adherence_Rate])), , DESC, DENSE),
        "DTC Observerd Rate", RANKX(ALLSELECTED(HHA), CALCULATE(SELECTEDVALUE(HHA[DTC_Observed_Rate])), , DESC, DENSE),
        "Fall injury Rate", RANKX(ALLSELECTED(HHA), CALCULATE(SELECTEDVALUE(HHA[Fall_injury_Rate])), , DESC, DENSE),
        "Flu Shot Rate", RANKX(ALLSELECTED(HHA), CALCULATE(SELECTEDVALUE(HHA[Flu_Shot_Rate])), , DESC, DENSE),
        "Info Transfer to Patient", RANKX(ALLSELECTED(HHA), CALCULATE(SELECTEDVALUE(HHA[Info_Transfer_to_Patient])), , DESC, DENSE),
        "Info Transfer to Provider", RANKX(ALLSELECTED(HHA), CALCULATE(SELECTEDVALUE(HHA[Info_Transfer_to_Provider])), , DESC, DENSE),
        "Patient Care Star Rating", RANKX(ALLSELECTED(HHA), CALCULATE(SELECTEDVALUE(HHA[Patient_Care_Star_Rating])), , DESC, DENSE),
        "PPH Observed Rate", RANKX(ALLSELECTED(HHA), CALCULATE(SELECTEDVALUE(HHA[PPH_Observed_Rate])), , DESC, DENSE),
        "PPR Observed Rate", RANKX(ALLSELECTED(HHA), CALCULATE(SELECTEDVALUE(HHA[PPR_Observed_Rate])), , DESC, DENSE),
        "Skin Integrity Change", RANKX(ALLSELECTED(HHA), CALCULATE(SELECTEDVALUE(HHA[Skin_Integrity_Change])), , DESC, DENSE),
        "Timely Care Start Rate", RANKX(ALLSELECTED(HHA), CALCULATE(SELECTEDVALUE(HHA[Timely_Care_Start_Rate])), , DESC, DENSE),
        "Timely Med Action Rate", RANKX(ALLSELECTED(HHA), CALCULATE(SELECTEDVALUE(HHA[Timely_Med_Action_Rate])), , DESC, DENSE),
        "Walking Improvement Rate", RANKX(ALLSELECTED(HHA), CALCULATE(SELECTEDVALUE(HHA[Walking_Improvement_Rate])), , DESC, DENSE)
    )
)
)

Rank_IRF = 
IF(
    SELECTEDVALUE(Quality_Measures_Sort[Name]) = "ASC",
    
    SWITCH(
        SELECTEDVALUE(IRF_Sort_By[Measures]),
        "CAUTI SIR", RANKX(ALLSELECTED(IRF), CALCULATE(SELECTEDVALUE(IRF[CAUTI_SIR])), , ASC, DENSE),
        "CDI SIR", RANKX(ALLSELECTED(IRF), CALCULATE(SELECTEDVALUE(IRF[CDI_SIR])), , ASC, DENSE),
        "DTC Observed Rate", RANKX(ALLSELECTED(IRF), CALCULATE(SELECTEDVALUE(IRF[DTC_Observed_Rate])), , ASC, DENSE),
        "Falls with Major Injury Rate", RANKX(ALLSELECTED(IRF), CALCULATE(SELECTEDVALUE(IRF[Falls_with_Major_Injury_Rate])), , ASC, DENSE),
        "Med List to Next Provider", RANKX(ALLSELECTED(IRF), CALCULATE(SELECTEDVALUE(IRF[Med_List_to_Next_Provider])), , ASC, DENSE),
        "Med List to Patient", RANKX(ALLSELECTED(IRF), CALCULATE(SELECTEDVALUE(IRF[Med_List_to_Patient])), , ASC, DENSE),
        "Med Review Follow-Up Rate", RANKX(ALLSELECTED(IRF), CALCULATE(SELECTEDVALUE(IRF[Med_Review_Follow_Up_Rate])), , ASC, DENSE),
        "Mobility Discharge Rate", RANKX(ALLSELECTED(IRF), CALCULATE(SELECTEDVALUE(IRF[Mobility_Discharge_Rate])), , ASC, DENSE),
        "Overall Self-Care & Mobility", RANKX(ALLSELECTED(IRF), CALCULATE(SELECTEDVALUE(IRF[Overall_Self_Care_Mobility])), , ASC, DENSE),
        "Personnel COVID-19 Vaccination Rate", RANKX(ALLSELECTED(IRF), CALCULATE(SELECTEDVALUE(IRF[Personnel_COVID_19_Vaccination_Rate])), , ASC, DENSE),
        "Personnel Flu Vaccination Rate", RANKX(ALLSELECTED(IRF), CALCULATE(SELECTEDVALUE(IRF[Personnel_Flu_Vaccination_Rate])), , ASC, DENSE),
        "PPR During Stay Rate", RANKX(ALLSELECTED(IRF), CALCULATE(SELECTEDVALUE(IRF[PPR_During_Stay_Rate])), , ASC, DENSE),
        "PPR Post-Discharge Rate", RANKX(ALLSELECTED(IRF), CALCULATE(SELECTEDVALUE(IRF[PPR_Post_Discharge_Rate])), , ASC, DENSE),
        "Pressure Injury Rate", RANKX(ALLSELECTED(IRF), CALCULATE(SELECTEDVALUE(IRF[Pressure_Injury_Rate])), , ASC, DENSE),
        "Self-Care Discharge Rate", RANKX(ALLSELECTED(IRF), CALCULATE(SELECTEDVALUE(IRF[Self_Care_Discharge_Rate])), , ASC, DENSE)
    ),

    SWITCH(
        SELECTEDVALUE(IRF_Sort_By[Measures]),
        "CAUTI SIR", RANKX(ALLSELECTED(IRF), CALCULATE(SELECTEDVALUE(IRF[CAUTI_SIR])), , DESC, DENSE),
        "CDI SIR", RANKX(ALLSELECTED(IRF), CALCULATE(SELECTEDVALUE(IRF[CDI_SIR])), , DESC, DENSE),
        "DTC Observed Rate", RANKX(ALLSELECTED(IRF), CALCULATE(SELECTEDVALUE(IRF[DTC_Observed_Rate])), , DESC, DENSE),
        "Falls with Major Injury Rate", RANKX(ALLSELECTED(IRF), CALCULATE(SELECTEDVALUE(IRF[Falls_with_Major_Injury_Rate])), , DESC, DENSE),
        "Med List to Next Provider", RANKX(ALLSELECTED(IRF), CALCULATE(SELECTEDVALUE(IRF[Med_List_to_Next_Provider])), , DESC, DENSE),
        "Med List to Patient", RANKX(ALLSELECTED(IRF), CALCULATE(SELECTEDVALUE(IRF[Med_List_to_Patient])), , DESC, DENSE),
        "Med Review Follow-Up Rate", RANKX(ALLSELECTED(IRF), CALCULATE(SELECTEDVALUE(IRF[Med_Review_Follow_Up_Rate])), , DESC, DENSE),
        "Mobility Discharge Rate", RANKX(ALLSELECTED(IRF), CALCULATE(SELECTEDVALUE(IRF[Mobility_Discharge_Rate])), , DESC, DENSE),
        "Overall Self-Care & Mobility", RANKX(ALLSELECTED(IRF), CALCULATE(SELECTEDVALUE(IRF[Overall_Self_Care_Mobility])), , DESC, DENSE),
        "Personnel COVID-19 Vaccination Rate", RANKX(ALLSELECTED(IRF), CALCULATE(SELECTEDVALUE(IRF[Personnel_COVID_19_Vaccination_Rate])), , DESC, DENSE),
        "Personnel Flu Vaccination Rate", RANKX(ALLSELECTED(IRF), CALCULATE(SELECTEDVALUE(IRF[Personnel_Flu_Vaccination_Rate])), , DESC, DENSE),
        "PPR During Stay Rate", RANKX(ALLSELECTED(IRF), CALCULATE(SELECTEDVALUE(IRF[PPR_During_Stay_Rate])), , DESC, DENSE),
        "PPR Post-Discharge Rate", RANKX(ALLSELECTED(IRF), CALCULATE(SELECTEDVALUE(IRF[PPR_Post_Discharge_Rate])), , DESC, DENSE),
        "Pressure Injury Rate", RANKX(ALLSELECTED(IRF), CALCULATE(SELECTEDVALUE(IRF[Pressure_Injury_Rate])), , DESC, DENSE),
        "Self-Care Discharge Rate", RANKX(ALLSELECTED(IRF), CALCULATE(SELECTEDVALUE(IRF[Self_Care_Discharge_Rate])), , DESC, DENSE)
    )
)

```
