### About data


| Data                         | Information                                     |
|------------------------------|-------------------------------------------------|
| Fullname dataset             | Contains full name.                             |
| All Indian Pincode directory | Contains office name, pincode, office type etc. |

Data that we get from AIPD include:
1. OfficeName
2. Pincode
3. OfficeType
4. DeliveryStatus
5. DivisionName
6. RegionName
7. CircleName
8. Taluk
9. DistrictName
10. StateName

So overall address, we will construct as:
* [OfficeName, 'comma', DivisionName, 'comma', RegionName, 'comma', CircleName, 'comma', 'Taluk', 'comma', 'DistrictName', 'comma', StateName]