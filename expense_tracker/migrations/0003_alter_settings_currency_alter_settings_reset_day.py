# Generated by Django 4.1.1 on 2022-09-28 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense_tracker', '0002_settings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='currency',
            field=models.CharField(choices=[('TND', 'TND'), ('ARA', 'ARA'), ('XBB', 'XBB'), ('KMF', 'KMF'), ('CYP', 'CYP'), ('DKK', 'DKK'), ('YUM', 'YUM'), ('AON', 'AON'), ('MTL', 'MTL'), ('ROL', 'ROL'), ('ECS', 'ECS'), ('DDM', 'DDM'), ('MKN', 'MKN'), ('IEP', 'IEP'), ('ZRZ', 'ZRZ'), ('PKR', 'PKR'), ('KYD', 'KYD'), ('YUN', 'YUN'), ('SEK', 'SEK'), ('BRE', 'BRE'), ('CHW', 'CHW'), ('NPR', 'NPR'), ('SLL', 'SLL'), ('TJS', 'TJS'), ('TMT', 'TMT'), ('NZD', 'NZD'), ('GMD', 'GMD'), ('XDR', 'XDR'), ('TWD', 'TWD'), ('SYP', 'SYP'), ('HRD', 'HRD'), ('XFO', 'XFO'), ('GQE', 'GQE'), ('SRD', 'SRD'), ('BZD', 'BZD'), ('CVE', 'CVE'), ('LSL', 'LSL'), ('GEK', 'GEK'), ('BAM', 'BAM'), ('XTS', 'XTS'), ('CHE', 'CHE'), ('KRH', 'KRH'), ('BYB', 'BYB'), ('GBP', 'GBP'), ('GEL', 'GEL'), ('VNN', 'VNN'), ('BND', 'BND'), ('HRK', 'HRK'), ('XBD', 'XBD'), ('BUK', 'BUK'), ('FRF', 'FRF'), ('SDG', 'SDG'), ('TZS', 'TZS'), ('LTT', 'LTT'), ('BEF', 'BEF'), ('BOL', 'BOL'), ('DOP', 'DOP'), ('XEU', 'XEU'), ('ISJ', 'ISJ'), ('UYP', 'UYP'), ('ECV', 'ECV'), ('PEI', 'PEI'), ('MZE', 'MZE'), ('SSP', 'SSP'), ('ZWR', 'ZWR'), ('XAF', 'XAF'), ('IDR', 'IDR'), ('BRZ', 'BRZ'), ('MZM', 'MZM'), ('RUB', 'RUB'), ('SKK', 'SKK'), ('SAR', 'SAR'), ('RWF', 'RWF'), ('HKD', 'HKD'), ('XPT', 'XPT'), ('THB', 'THB'), ('LKR', 'LKR'), ('CHF', 'CHF'), ('SZL', 'SZL'), ('ESB', 'ESB'), ('LUF', 'LUF'), ('STN', 'STN'), ('RON', 'RON'), ('ISK', 'ISK'), ('BOP', 'BOP'), ('BAN', 'BAN'), ('KRW', 'KRW'), ('MAF', 'MAF'), ('MMK', 'MMK'), ('UGS', 'UGS'), ('ILS', 'ILS'), ('ARL', 'ARL'), ('ARS', 'ARS'), ('UZS', 'UZS'), ('MZN', 'MZN'), ('UYU', 'UYU'), ('EUR', 'EUR'), ('BYR', 'BYR'), ('CUC', 'CUC'), ('IRR', 'IRR'), ('KZT', 'KZT'), ('ETB', 'ETB'), ('CUP', 'CUP'), ('SDD', 'SDD'), ('VEF', 'VEF'), ('ALL', 'ALL'), ('MUR', 'MUR'), ('DEM', 'DEM'), ('CNY', 'CNY'), ('WST', 'WST'), ('LYD', 'LYD'), ('SLE', 'SLE'), ('MKD', 'MKD'), ('ARP', 'ARP'), ('NIC', 'NIC'), ('UYI', 'UYI'), ('MXN', 'MXN'), ('SVC', 'SVC'), ('LTL', 'LTL'), ('GNF', 'GNF'), ('MLF', 'MLF'), ('CLP', 'CLP'), ('MTP', 'MTP'), ('ALK', 'ALK'), ('AWG', 'AWG'), ('EGP', 'EGP'), ('GWP', 'GWP'), ('INR', 'INR'), ('BRB', 'BRB'), ('TRL', 'TRL'), ('BRR', 'BRR'), ('MYR', 'MYR'), ('CLE', 'CLE'), ('QAR', 'QAR'), ('KES', 'KES'), ('AFN', 'AFN'), ('KRO', 'KRO'), ('VED', 'VED'), ('UGX', 'UGX'), ('SUR', 'SUR'), ('OMR', 'OMR'), ('ILP', 'ILP'), ('ZWL', 'ZWL'), ('BMD', 'BMD'), ('XSU', 'XSU'), ('AED', 'AED'), ('BEL', 'BEL'), ('VUV', 'VUV'), ('CRC', 'CRC'), ('SHP', 'SHP'), ('BGM', 'BGM'), ('BOV', 'BOV'), ('LVR', 'LVR'), ('FKP', 'FKP'), ('XOF', 'XOF'), ('AMD', 'AMD'), ('BRL', 'BRL'), ('LBP', 'LBP'), ('MNT', 'MNT'), ('PTE', 'PTE'), ('LVL', 'LVL'), ('GYD', 'GYD'), ('YUR', 'YUR'), ('MWK', 'MWK'), ('AFA', 'AFA'), ('ERN', 'ERN'), ('BSD', 'BSD'), ('PYG', 'PYG'), ('SRG', 'SRG'), ('XPD', 'XPD'), ('EEK', 'EEK'), ('KGS', 'KGS'), ('ZAR', 'ZAR'), ('AZM', 'AZM'), ('GRD', 'GRD'), ('USN', 'USN'), ('MCF', 'MCF'), ('VES', 'VES'), ('YDD', 'YDD'), ('ATS', 'ATS'), ('BTN', 'BTN'), ('CAD', 'CAD'), ('HTG', 'HTG'), ('XRE', 'XRE'), ('AZN', 'AZN'), ('ILR', 'ILR'), ('AOK', 'AOK'), ('GTQ', 'GTQ'), ('HNL', 'HNL'), ('SOS', 'SOS'), ('AOA', 'AOA'), ('VEB', 'VEB'), ('LUC', 'LUC'), ('BYN', 'BYN'), ('BGO', 'BGO'), ('PGK', 'PGK'), ('MOP', 'MOP'), ('XBA', 'XBA'), ('AUD', 'AUD'), ('BIF', 'BIF'), ('SGD', 'SGD'), ('UAH', 'UAH'), ('TTD', 'TTD'), ('BOB', 'BOB'), ('AOR', 'AOR'), ('LAK', 'LAK'), ('LRD', 'LRD'), ('MGF', 'MGF'), ('XCD', 'XCD'), ('XPF', 'XPF'), ('PHP', 'PHP'), ('SBD', 'SBD'), ('PAB', 'PAB'), ('HUF', 'HUF'), ('BHD', 'BHD'), ('CZK', 'CZK'), ('RUR', 'RUR'), ('FIM', 'FIM'), ('BDT', 'BDT'), ('PEN', 'PEN'), ('BBD', 'BBD'), ('KHR', 'KHR'), ('UYW', 'UYW'), ('SIT', 'SIT'), ('NGN', 'NGN'), ('XBC', 'XBC'), ('ZMK', 'ZMK'), ('FJD', 'FJD'), ('CDF', 'CDF'), ('MVR', 'MVR'), ('CLF', 'CLF'), ('CNX', 'CNX'), ('XAU', 'XAU'), ('STD', 'STD'), ('IQD', 'IQD'), ('XUA', 'XUA'), ('BEC', 'BEC'), ('XFU', 'XFU'), ('TJR', 'TJR'), ('NOK', 'NOK'), ('JMD', 'JMD'), ('ESP', 'ESP'), ('PLZ', 'PLZ'), ('NAD', 'NAD'), ('BRC', 'BRC'), ('TRY', 'TRY'), ('CSK', 'CSK'), ('JPY', 'JPY'), ('UAK', 'UAK'), ('MXP', 'MXP'), ('GHS', 'GHS'), ('MDC', 'MDC'), ('TPE', 'TPE'), ('COU', 'COU'), ('MRO', 'MRO'), ('MRU', 'MRU'), ('GWE', 'GWE'), ('TMM', 'TMM'), ('JOD', 'JOD'), ('ARM', 'ARM'), ('BRN', 'BRN'), ('ADP', 'ADP'), ('YER', 'YER'), ('USD', 'USD'), ('COP', 'COP'), ('RHD', 'RHD'), ('KPW', 'KPW'), ('SDP', 'SDP'), ('XAG', 'XAG'), ('MGA', 'MGA'), ('DZD', 'DZD'), ('BAD', 'BAD'), ('GNS', 'GNS'), ('VND', 'VND'), ('RSD', 'RSD'), ('GIP', 'GIP'), ('XXX', 'XXX'), ('TOP', 'TOP'), ('YUD', 'YUD'), ('NLG', 'NLG'), ('USS', 'USS'), ('ZAL', 'ZAL'), ('ESA', 'ESA'), ('BGL', 'BGL'), ('BWP', 'BWP'), ('CSD', 'CSD'), ('KWD', 'KWD'), ('DJF', 'DJF'), ('ITL', 'ITL'), ('ANG', 'ANG'), ('PLN', 'PLN'), ('BGN', 'BGN'), ('CNH', 'CNH'), ('GHC', 'GHC'), ('MVP', 'MVP'), ('SCR', 'SCR'), ('ZWD', 'ZWD'), ('NIO', 'NIO'), ('MXV', 'MXV'), ('ZRN', 'ZRN'), ('ZMW', 'ZMW'), ('MDL', 'MDL'), ('MAD', 'MAD'), ('LUL', 'LUL'), ('PES', 'PES')], default='USD', max_length=3),
        ),
        migrations.AlterField(
            model_name='settings',
            name='reset_day',
            field=models.IntegerField(default='1'),
        ),
    ]
