# Generated by Django 3.2.8 on 2022-01-16 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cooperative', '0052_itemwriteoffreasons'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='accountdeductions',
            table='accountdeductions',
        ),
        migrations.AlterModelTable(
            name='approvabletransactions',
            table='approvabletransactions',
        ),
        migrations.AlterModelTable(
            name='approvalofficers',
            table='approvalofficers',
        ),
        migrations.AlterModelTable(
            name='autoreceipt',
            table='autoreceipt',
        ),
        migrations.AlterModelTable(
            name='certifiabletransactions',
            table='certifiabletransactions',
        ),
        migrations.AlterModelTable(
            name='certificationofficers',
            table='certificationofficers',
        ),
        migrations.AlterModelTable(
            name='compulsorysavings',
            table='compulsorysavings',
        ),
        migrations.AlterModelTable(
            name='cooperativebankaccounts',
            table='cooperativebankaccounts',
        ),
        migrations.AlterModelTable(
            name='disbursementofficers',
            table='disbursementofficers',
        ),
        migrations.AlterModelTable(
            name='externalfascilitiesmain',
            table='externalfascilitiesmain',
        ),
        migrations.AlterModelTable(
            name='externalfascilitiestemp',
            table='externalfascilitiestemp',
        ),
        migrations.AlterModelTable(
            name='lga',
            table='lga',
        ),
        migrations.AlterModelTable(
            name='loanapplication',
            table='loanApplication',
        ),
        migrations.AlterModelTable(
            name='loanapplicationguarnators',
            table='loanapplicationguarnators',
        ),
        migrations.AlterModelTable(
            name='loanapplicationsettings',
            table='loanapplicationsettings',
        ),
        migrations.AlterModelTable(
            name='loanbasedsavings',
            table='loanbasedsavings',
        ),
        migrations.AlterModelTable(
            name='loanformissuance',
            table='loanformissuance',
        ),
        migrations.AlterModelTable(
            name='loanguarantors',
            table='loanguarantors',
        ),
        migrations.AlterModelTable(
            name='loannumber',
            table='loannumber',
        ),
        migrations.AlterModelTable(
            name='loanrequest',
            table='loanrequest',
        ),
        migrations.AlterModelTable(
            name='loanrequestattachments',
            table='loanrequestattachments',
        ),
        migrations.AlterModelTable(
            name='loanrequestsettings',
            table='loanrequestsettings',
        ),
        migrations.AlterModelTable(
            name='loanscleared',
            table='loanscleared',
        ),
        migrations.AlterModelTable(
            name='loansdisbursed',
            table='loansdisbursed',
        ),
        migrations.AlterModelTable(
            name='loansrepaymentbase',
            table='loansrepaymentBase',
        ),
        migrations.AlterModelTable(
            name='loansuploaded',
            table='loansuploaded',
        ),
        migrations.AlterModelTable(
            name='members',
            table='members',
        ),
        migrations.AlterModelTable(
            name='membersaccountsdomain',
            table='membersaccountsdomain',
        ),
        migrations.AlterModelTable(
            name='membersbankaccounts',
            table='membersbankaccounts',
        ),
        migrations.AlterModelTable(
            name='membersexclusiveness',
            table='membersexclusiveness',
        ),
        migrations.AlterModelTable(
            name='membershipformsalesrecord',
            table='membershipformsalesrecord',
        ),
        migrations.AlterModelTable(
            name='membershiprequest',
            table='membershiprequest',
        ),
        migrations.AlterModelTable(
            name='membershiprequestadditionalinfo',
            table='memberShiprequestadditionalinfo',
        ),
        migrations.AlterModelTable(
            name='membersidmanager',
            table='membersidmanager',
        ),
        migrations.AlterModelTable(
            name='membersnextofkins',
            table='membersnextofkins',
        ),
        migrations.AlterModelTable(
            name='memberssalaryupdaterequest',
            table='memberssalaryupdaterequest',
        ),
        migrations.AlterModelTable(
            name='monthlydeductionlist',
            table='monthlydeductionlist',
        ),
        migrations.AlterModelTable(
            name='monthlydeductionlistgenerated',
            table='monthlydeductionlistgenerated',
        ),
        migrations.AlterModelTable(
            name='monthlygeneratedtransactions',
            table='monthlygeneratedtransactions',
        ),
        migrations.AlterModelTable(
            name='monthlygroupgeneratedtransactions',
            table='monthlygroupgeneratedtransactions',
        ),
        migrations.AlterModelTable(
            name='nextofkinsmaximun',
            table='nextofkinsmaximun',
        ),
        migrations.AlterModelTable(
            name='nonmemberaccountdeductions',
            table='nonMemberaccountdeductions',
        ),
        migrations.AlterModelTable(
            name='norminalroll',
            table='norminalroll',
        ),
        migrations.AlterModelTable(
            name='receipt_cancelled',
            table='receiptcancelled',
        ),
        migrations.AlterModelTable(
            name='receipts',
            table='receipts',
        ),
        migrations.AlterModelTable(
            name='receipts_shop',
            table='receipts_shop',
        ),
        migrations.AlterModelTable(
            name='savingsuploaded',
            table='savingsuploaded',
        ),
        migrations.AlterModelTable(
            name='sharesdeductionsavings',
            table='sharesdeductionsavings',
        ),
        migrations.AlterModelTable(
            name='sharesunits',
            table='sharesunits',
        ),
        migrations.AlterModelTable(
            name='staff',
            table='staff',
        ),
        migrations.AlterModelTable(
            name='standingorderaccounts',
            table='standingorderaccounts',
        ),
        migrations.AlterModelTable(
            name='transactionajustmentrequest',
            table='transactionadjustmentRequest',
        ),
        migrations.AlterModelTable(
            name='transactionloanajustmentrequest',
            table='transactionLoanadjustmentrequest',
        ),
        migrations.AlterModelTable(
            name='transactiontypes',
            table='transactiontypes',
        ),
        migrations.AlterModelTable(
            name='withdrawabletransactions',
            table='Withdrawabletransactions',
        ),
    ]
