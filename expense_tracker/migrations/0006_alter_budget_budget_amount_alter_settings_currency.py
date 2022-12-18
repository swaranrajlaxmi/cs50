# Generated by Django 4.1.1 on 2022-10-07 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense_tracker', '0005_alter_settings_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='budget_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='settings',
            name='currency',
            field=models.CharField(choices=[('AOK', 'AOK'), ('PEN', 'PEN'), ('YER', 'YER'), ('VEB', 'VEB'), ('LTL', 'LTL'), ('AZM', 'AZM'), ('BAD', 'BAD'), ('STD', 'STD'), ('LAK', 'LAK'), ('XAF', 'XAF'), ('FIM', 'FIM'), ('BWP', 'BWP'), ('ZRN', 'ZRN'), ('GYD', 'GYD'), ('KYD', 'KYD'), ('NLG', 'NLG'), ('ITL', 'ITL'), ('MRO', 'MRO'), ('BEL', 'BEL'), ('NIO', 'NIO'), ('WST', 'WST'), ('RWF', 'RWF'), ('PAB', 'PAB'), ('UYW', 'UYW'), ('GBP', 'GBP'), ('LVR', 'LVR'), ('RUB', 'RUB'), ('LVL', 'LVL'), ('GMD', 'GMD'), ('TOP', 'TOP'), ('THB', 'THB'), ('BUK', 'BUK'), ('SDG', 'SDG'), ('XCD', 'XCD'), ('MTL', 'MTL'), ('SEK', 'SEK'), ('XTS', 'XTS'), ('ERN', 'ERN'), ('DOP', 'DOP'), ('VES', 'VES'), ('ETB', 'ETB'), ('FRF', 'FRF'), ('UYP', 'UYP'), ('BYR', 'BYR'), ('SYP', 'SYP'), ('UAH', 'UAH'), ('MWK', 'MWK'), ('GQE', 'GQE'), ('KWD', 'KWD'), ('VND', 'VND'), ('HKD', 'HKD'), ('NIC', 'NIC'), ('MDC', 'MDC'), ('MVR', 'MVR'), ('CVE', 'CVE'), ('BSD', 'BSD'), ('MGA', 'MGA'), ('GRD', 'GRD'), ('PLN', 'PLN'), ('SIT', 'SIT'), ('RHD', 'RHD'), ('CYP', 'CYP'), ('ZWR', 'ZWR'), ('SSP', 'SSP'), ('HRD', 'HRD'), ('AZN', 'AZN'), ('MZN', 'MZN'), ('BRB', 'BRB'), ('YUR', 'YUR'), ('ESP', 'ESP'), ('SAR', 'SAR'), ('XBB', 'XBB'), ('JOD', 'JOD'), ('CLP', 'CLP'), ('XAG', 'XAG'), ('BOL', 'BOL'), ('DEM', 'DEM'), ('ESB', 'ESB'), ('ANG', 'ANG'), ('GEK', 'GEK'), ('MAF', 'MAF'), ('KGS', 'KGS'), ('XPF', 'XPF'), ('AFA', 'AFA'), ('TPE', 'TPE'), ('ARS', 'ARS'), ('BOB', 'BOB'), ('ISK', 'ISK'), ('SDP', 'SDP'), ('COP', 'COP'), ('BRZ', 'BRZ'), ('KRO', 'KRO'), ('DDM', 'DDM'), ('ALK', 'ALK'), ('AOR', 'AOR'), ('XOF', 'XOF'), ('BAM', 'BAM'), ('BGM', 'BGM'), ('DZD', 'DZD'), ('ADP', 'ADP'), ('DJF', 'DJF'), ('SDD', 'SDD'), ('GWP', 'GWP'), ('BRL', 'BRL'), ('IDR', 'IDR'), ('XBD', 'XBD'), ('TND', 'TND'), ('MXV', 'MXV'), ('ISJ', 'ISJ'), ('KRH', 'KRH'), ('CSK', 'CSK'), ('LSL', 'LSL'), ('ARP', 'ARP'), ('ARL', 'ARL'), ('IRR', 'IRR'), ('TJR', 'TJR'), ('LUL', 'LUL'), ('SLE', 'SLE'), ('CHF', 'CHF'), ('TTD', 'TTD'), ('PEI', 'PEI'), ('FKP', 'FKP'), ('USD', 'USD'), ('KPW', 'KPW'), ('NOK', 'NOK'), ('LUF', 'LUF'), ('LYD', 'LYD'), ('MYR', 'MYR'), ('CNX', 'CNX'), ('CLE', 'CLE'), ('RSD', 'RSD'), ('PHP', 'PHP'), ('UGS', 'UGS'), ('XFO', 'XFO'), ('ZWD', 'ZWD'), ('INR', 'INR'), ('ECV', 'ECV'), ('XSU', 'XSU'), ('SLL', 'SLL'), ('MUR', 'MUR'), ('NGN', 'NGN'), ('BZD', 'BZD'), ('FJD', 'FJD'), ('MVP', 'MVP'), ('PES', 'PES'), ('GEL', 'GEL'), ('SUR', 'SUR'), ('KHR', 'KHR'), ('MTP', 'MTP'), ('JPY', 'JPY'), ('USN', 'USN'), ('AFN', 'AFN'), ('MKD', 'MKD'), ('XDR', 'XDR'), ('BTN', 'BTN'), ('EUR', 'EUR'), ('GNS', 'GNS'), ('MAD', 'MAD'), ('BYB', 'BYB'), ('GNF', 'GNF'), ('MXP', 'MXP'), ('UAK', 'UAK'), ('CUP', 'CUP'), ('IQD', 'IQD'), ('TRY', 'TRY'), ('ZAR', 'ZAR'), ('VEF', 'VEF'), ('KES', 'KES'), ('LTT', 'LTT'), ('SZL', 'SZL'), ('XRE', 'XRE'), ('AED', 'AED'), ('VUV', 'VUV'), ('SRG', 'SRG'), ('RUR', 'RUR'), ('ZMK', 'ZMK'), ('XBA', 'XBA'), ('XPD', 'XPD'), ('MNT', 'MNT'), ('SKK', 'SKK'), ('CNY', 'CNY'), ('XUA', 'XUA'), ('KZT', 'KZT'), ('MRU', 'MRU'), ('BGO', 'BGO'), ('MZM', 'MZM'), ('CAD', 'CAD'), ('GWE', 'GWE'), ('ZAL', 'ZAL'), ('MXN', 'MXN'), ('LRD', 'LRD'), ('UGX', 'UGX'), ('AOA', 'AOA'), ('TWD', 'TWD'), ('RON', 'RON'), ('JMD', 'JMD'), ('MOP', 'MOP'), ('SHP', 'SHP'), ('PKR', 'PKR'), ('ILS', 'ILS'), ('EGP', 'EGP'), ('BOV', 'BOV'), ('ZRZ', 'ZRZ'), ('BEF', 'BEF'), ('XFU', 'XFU'), ('BEC', 'BEC'), ('AMD', 'AMD'), ('TJS', 'TJS'), ('HNL', 'HNL'), ('BRR', 'BRR'), ('TMT', 'TMT'), ('AON', 'AON'), ('BMD', 'BMD'), ('BRE', 'BRE'), ('LUC', 'LUC'), ('TZS', 'TZS'), ('BND', 'BND'), ('CDF', 'CDF'), ('HTG', 'HTG'), ('IEP', 'IEP'), ('CUC', 'CUC'), ('BDT', 'BDT'), ('TRL', 'TRL'), ('OMR', 'OMR'), ('ARM', 'ARM'), ('CRC', 'CRC'), ('XBC', 'XBC'), ('SVC', 'SVC'), ('GIP', 'GIP'), ('VNN', 'VNN'), ('ECS', 'ECS'), ('PLZ', 'PLZ'), ('BIF', 'BIF'), ('ZWL', 'ZWL'), ('AWG', 'AWG'), ('SBD', 'SBD'), ('SRD', 'SRD'), ('NAD', 'NAD'), ('LKR', 'LKR'), ('HUF', 'HUF'), ('MDL', 'MDL'), ('MCF', 'MCF'), ('GHS', 'GHS'), ('CLF', 'CLF'), ('MZE', 'MZE'), ('YUN', 'YUN'), ('DKK', 'DKK'), ('ESA', 'ESA'), ('SGD', 'SGD'), ('YUD', 'YUD'), ('BGN', 'BGN'), ('VED', 'VED'), ('ALL', 'ALL'), ('MMK', 'MMK'), ('BOP', 'BOP'), ('BRN', 'BRN'), ('CNH', 'CNH'), ('ILP', 'ILP'), ('NPR', 'NPR'), ('CHW', 'CHW'), ('XPT', 'XPT'), ('KRW', 'KRW'), ('EEK', 'EEK'), ('SOS', 'SOS'), ('MLF', 'MLF'), ('SCR', 'SCR'), ('STN', 'STN'), ('XXX', 'XXX'), ('NZD', 'NZD'), ('XAU', 'XAU'), ('UYI', 'UYI'), ('YDD', 'YDD'), ('AUD', 'AUD'), ('XEU', 'XEU'), ('ZMW', 'ZMW'), ('PYG', 'PYG'), ('TMM', 'TMM'), ('KMF', 'KMF'), ('MGF', 'MGF'), ('PTE', 'PTE'), ('BGL', 'BGL'), ('YUM', 'YUM'), ('ATS', 'ATS'), ('QAR', 'QAR'), ('GHC', 'GHC'), ('HRK', 'HRK'), ('BAN', 'BAN'), ('MKN', 'MKN'), ('CZK', 'CZK'), ('COU', 'COU'), ('USS', 'USS'), ('BBD', 'BBD'), ('CSD', 'CSD'), ('PGK', 'PGK'), ('CHE', 'CHE'), ('UZS', 'UZS'), ('BRC', 'BRC'), ('GTQ', 'GTQ'), ('ILR', 'ILR'), ('LBP', 'LBP'), ('ROL', 'ROL'), ('UYU', 'UYU'), ('ARA', 'ARA'), ('BHD', 'BHD'), ('BYN', 'BYN')], default='USD', max_length=3),
        ),
    ]