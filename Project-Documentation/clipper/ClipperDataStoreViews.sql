
CREATE VIEW [dbo].[AddValueTransactions] AS
 SELECT	AV.OperatorID,
	P.ParticipantName,
	AV.SecurityModuleID,
	AV.DeviceSerialNumber,
	AV.VehicleID,
	AV.RouteID,
	R.RouteName,
	AV.SequenceNumber,
	AV.GenerationTime,
	AV.RecordType,
	AV.SubType,
	AV.ApplicationSerialNumber AS CardID,
	AV.ApplicationTransactionSequenceNumber AS CardIDSequenceNumber,
	AV.TransactionQualifierNegativeFare,
	AV.TransactionQualifierSpecialFailure,
	AV.ContractSequenceNumber,
	AV.ContractID,
	AV.ContractSerialNumber,
	AV.ValueAddedTransLinkECash,
	AV.ValueAddedPeriodPass,
	AV.ValueAddedMultiRide,
	AV.ValueAddedGenericECash,
	AV.UpdatedValueTransLinkECash,
	AV.UpdatedValuePeriodPass,
	AV.UpdatedValueMultiRide,
	AV.UpdatedValueGenericECash,
	AV.OriginLocation,
	OL.LocationName AS OriginLocationName,
	AV.DestinationLocation,
	DL.LocationName As DestinationLocationName,
	AV.PurchasePrice,
	AV.StartDate,
	AV.ExpiryDate,
	AV.CashPaymentPurchasePrice,
	AV.CheckPaymentPurchasePrice,
	AV.CreditCardPaymentPurchasePrice,
	AV.DebitCardPaymentPurchasePrice,
	AV.InstitutionalPass
 FROM SfoAddValueTransaction AV
	LEFT OUTER JOIN Participants P ON AV.OperatorID = P.ParticipantID
	LEFT OUTER JOIN Routes R ON AV.OperatorID = R.ParticipantID AND AV.RouteID = R.RouteID
	LEFT OUTER JOIN Locations OL ON AV.OriginLocation = OL.LocationCode AND AV.OperatorID = OL.ParticipantID
	LEFT OUTER JOIN Locations DL ON AV.DestinationLocation = DL.LocationCode AND AV.OperatorID = DL.ParticipantID;


CREATE VIEW [dbo].[BusinessRulesFailure] AS
 SELECT	BRF.OperatorID,
	P.ParticipantName,
	BRF.SecurityModuleID,
	BRF.DeviceSerialNumber,
	BRF.VehicleID,
	BRF.RouteID,
	R.RouteName,
	BRF.SequenceNumber,
	BRF.GenerationTime,
	BRF.RecordType,
	BRF.SubType,
	BRF.ApplicationSerialNumber AS CardID,
	BRF.ApplicationTransactionSequenceNumber AS CardIDSequenceNumber,
	BRF.ContractID,
	BRF.ContractSerialNumber,
	BRF.ContractFlags,
	BRF.ContractStatus,
	BRF.FareCategory,
	BRF.ReasonCode,
	BRF.PurseBalance
 FROM SfoBusinessRulesFailure BRF
	LEFT OUTER JOIN Participants P ON BRF.OperatorID = P.ParticipantID
	LEFT OUTER JOIN Routes R ON BRF.OperatorID = R.ParticipantID AND BRF.RouteID = R.RouteID;


CREATE VIEW [dbo].[FareTransactions] AS
 SELECT	F.OperatorID,
	P.ParticipantName,
	F.DeviceSerialNumber,
	F.VehicleID,
	F.RouteID,
	R.RouteName,
	F.SequenceNumber,
	F.GenerationTime,
	F.SubType,
	F.ApplicationSerialNumber AS CardID,
	F.ApplicationTransactionSequenceNumber AS CardIDSequenceNumber,
	F.ContractID,
	F.ContractSerialNumber,
	F.PurseAmount,
	F.PurseBalance,
	F.FareCategory,
	F.TransferOperator,
	TP.ParticipantName AS TransferOperatorName,
	F.TransferDiscountFlag,
	F.OriginLocation,
	OL.LocationName AS OriginLocationName,
	F.DestinationLocation,
	DL.LocationName As DestinationLocationName,
	F.RideAnnulled,
	F.StartTime,
	F.InstitutionID,
	REPLACE(STR(TripSequenceNumber,5),' ','0') AS TripNumber
 FROM SfoFareTransaction F
	LEFT OUTER JOIN Participants P ON F.OperatorID = P.ParticipantID
	LEFT OUTER JOIN Routes R ON F.OperatorID = R.ParticipantID AND F.RouteID = R.RouteID
	LEFT OUTER JOIN Participants TP ON F.TransferOperator = TP.ParticipantID
	LEFT OUTER JOIN Locations OL ON F.OriginLocation = OL.LocationCode AND F.OperatorID = OL.ParticipantID
	LEFT OUTER JOIN Locations DL ON F.DestinationLocation = DL.LocationCode AND F.OperatorID = DL.ParticipantID;

    
CREATE VIEW [dbo].[TOTAddValueTransactions] AS
 SELECT	TOTAV.OperatorID,
	P.ParticipantName,
	TOTAV.SecurityModuleID,
	TOTAV.DeviceSerialNumber,
	TOTAV.VehicleID,
	TOTAV.RouteID,
	R.RouteName,
	TOTAV.SequenceNumber,
	TOTAV.GenerationTime,
	TOTAV.RecordType,
	TOTAV.SubType,
	TOTAV.ApplicationSerialNumber AS CardID,
	TOTAV.ApplicationTransactionSequenceNumber AS CardIDSequenceNumber,
	TOTAV.TransactionQualifierNegativeFare,
	TOTAV.TransactionQualifierSpecialFailure,
	TOTAV.ContractSequenceNumber,
	TOTAV.ContractID,
	TOTAV.ContractSerialNumber,
	TOTAV.ValueAddedTransLinkECash,
	TOTAV.ValueAddedPeriodPass,
	TOTAV.ValueAddedMultiRide,
	TOTAV.ValueAddedGenericECash,
	TOTAV.UpdatedValueTransLinkECash,
	TOTAV.UpdatedValuePeriodPass,
	TOTAV.UpdatedValueMultiRide,
	TOTAV.UpdatedValueGenericECash,
	TOTAV.OriginLocation,
	OL.LocationName AS OriginLocationName,
	TOTAV.DestinationLocation,
	DL.LocationName As DestinationLocationName,
	TOTAV.TotalPayment,
	TOTAV.ReceiptNumber,
	TOTAV.NumberOfPaymentItems
 FROM SfoTOTAddValueTransaction TOTAV
	LEFT OUTER JOIN Participants P ON TOTAV.OperatorID = P.ParticipantID
	LEFT OUTER JOIN Routes R ON TOTAV.OperatorID = R.ParticipantID AND TOTAV.RouteID = R.RouteID
	LEFT OUTER JOIN Locations OL ON TOTAV.OriginLocation = OL.LocationCode AND TOTAV.OperatorID = OL.ParticipantID
	LEFT OUTER JOIN Locations DL ON TOTAV.DestinationLocation = DL.LocationCode AND TOTAV.OperatorID = DL.ParticipantID;

    
CREATE VIEW [dbo].[VAddValueTransactions] AS
 SELECT	OperatorID,
	ParticipantName,
	SecurityModuleID,
	DeviceSerialNumber,
	VehicleID,
	RouteID,
	RouteName,
	SequenceNumber,
	CAST(CAST(DATEPART(year,GenerationTime) AS CHAR(4)) + '-' + REPLACE(CAST(DATEPART(month,GenerationTime) AS CHAR(2)),' ','0') + '-' + REPLACE(CAST(DATEPART(day,GenerationTime) AS CHAR(2)),' ','0') AS DATETIME) AS TransactionDate,
	GenerationTime AS TransactionTime,
	RecordType,
	SubType,
	CardID,
	CardIDSequenceNumber,
	TransactionQualifierNegativeFare,
	TransactionQualifierSpecialFailure,
	ContractSequenceNumber,
	ContractID,
	ContractSerialNumber,
	ValueAddedTransLinkECash,
	ValueAddedPeriodPass,
	ValueAddedMultiRide,
	ValueAddedGenericECash,
	UpdatedValueTransLinkECash,
	UpdatedValuePeriodPass,
	UpdatedValueMultiRide,
	UpdatedValueGenericECash,
	OriginLocation,
	OriginLocationName,
	DestinationLocation,
	DestinationLocationName,
	PurchasePrice,
	StartDate,
	ExpiryDate,
	CashPaymentPurchasePrice,
	CheckPaymentPurchasePrice,
	CreditCardPaymentPurchasePrice,
	DebitCardPaymentPurchasePrice,
	InstitutionalPass
 FROM AddValueTransactions;

 
CREATE VIEW [dbo].[VBusinessRulesFailure] AS
 SELECT	OperatorID,
	ParticipantName,
	SecurityModuleID,
	DeviceSerialNumber,
	VehicleID,
	RouteID,
	RouteName,
	SequenceNumber,
	CAST(CAST(DATEPART(year,GenerationTime) AS CHAR(4)) + '-' + REPLACE(CAST(DATEPART(month,GenerationTime) AS CHAR(2)),' ','0') + '-' + REPLACE(CAST(DATEPART(day,GenerationTime) AS CHAR(2)),' ','0') AS DATETIME) AS TransactionDate,
	GenerationTime AS TransactionTime,
	RecordType,
	SubType,
	CardID,
	CardIDSequenceNumber,
	ContractID,
	ContractSerialNumber,
	ContractFlags,
	ContractStatus,
	FareCategory,
	ReasonCode,
	PurseBalance
 FROM BusinessRulesFailure;

 
create view [dbo].[VDeviceLocations] as
select dl.DeviceID,
       dl.ModelID,
       dl.VehicleID,
       dl.PlaceID,
       dl.LocationName,
       dl.SubLocation,
       dl.InstallDate LatestInstallDate,
       dl.DeInstallDate,
       mindl.FirstInstallDate
 from (select DeviceID,max(InstallDate) LatestInstallDate
        from dbo.DeviceLocation
        group by DeviceID) maxdl
  inner join dbo.DeviceLocation dl
    on maxdl.DeviceID = dl.DeviceID and maxdl.LatestInstallDate = dl.InstallDate
  inner join (select DeviceID,min(InstallDate) FirstInstallDate
        from dbo.DeviceLocation
        group by DeviceID) mindl
    on maxdl.DeviceID = mindl.DeviceID;


CREATE VIEW [dbo].[VTOTAddValueTransactions] AS
 SELECT	OperatorID,
	ParticipantName,
	SecurityModuleID,
	DeviceSerialNumber,
	VehicleID,
	RouteID,
	RouteName,
	SequenceNumber,
	CAST(CAST(DATEPART(year,GenerationTime) AS CHAR(4)) + '-' + REPLACE(CAST(DATEPART(month,GenerationTime) AS CHAR(2)),' ','0') + '-' + REPLACE(CAST(DATEPART(day,GenerationTime) AS CHAR(2)),' ','0') AS DATETIME) AS TransactionDate,
	GenerationTime AS TransactionTime,
	RecordType,
	SubType,
	CardID,
	CardIDSequenceNumber,
	TransactionQualifierNegativeFare,
	TransactionQualifierSpecialFailure,
	ContractSequenceNumber,
	ContractID,
	ContractSerialNumber,
	ValueAddedTransLinkECash,
	ValueAddedPeriodPass,
	ValueAddedMultiRide,
	ValueAddedGenericECash,
	UpdatedValueTransLinkECash,
	UpdatedValuePeriodPass,
	UpdatedValueMultiRide,
	UpdatedValueGenericECash,
	OriginLocation,
	OriginLocationName,
	DestinationLocation,
	DestinationLocationName,
	TotalPayment,
	ReceiptNumber,
	NumberOfPaymentItems
 FROM TOTAddValueTransactions;

 CREATE VIEW dbo.vOperatorbyProductTypeSept2013
AS
SELECT     OperatorID, ContractID, FareCategory, COUNT(*) AS total
FROM         dbo.SfoFareTransaction AS t
WHERE     (GenerationTime >= '9/1/2013') AND (GenerationTime <= '9/30/2013') AND (OperatorID IN (1, 4, 6, 25, 11, 101, 15, 18, 100, 17, 27))
GROUP BY OperatorID, ContractID, FareCategory;







