# Generated by Django 4.1.1 on 2022-09-28 07:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expense_tracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(choices=[('MTL', 'MTL'), ('ALK', 'ALK'), ('BAN', 'BAN'), ('DOP', 'DOP'), ('KZT', 'KZT'), ('CNX', 'CNX'), ('TMM', 'TMM'), ('PAB', 'PAB'), ('CAD', 'CAD'), ('GRD', 'GRD'), ('BRE', 'BRE'), ('GTQ', 'GTQ'), ('RON', 'RON'), ('AZN', 'AZN'), ('BSD', 'BSD'), ('MAD', 'MAD'), ('JOD', 'JOD'), ('KMF', 'KMF'), ('AZM', 'AZM'), ('JPY', 'JPY'), ('WST', 'WST'), ('LSL', 'LSL'), ('LTT', 'LTT'), ('DKK', 'DKK'), ('MLF', 'MLF'), ('OMR', 'OMR'), ('YDD', 'YDD'), ('XPF', 'XPF'), ('RUB', 'RUB'), ('MZM', 'MZM'), ('CHF', 'CHF'), ('SUR', 'SUR'), ('LRD', 'LRD'), ('BOB', 'BOB'), ('XBB', 'XBB'), ('XAU', 'XAU'), ('LUL', 'LUL'), ('BZD', 'BZD'), ('KYD', 'KYD'), ('MNT', 'MNT'), ('SLL', 'SLL'), ('MVR', 'MVR'), ('UYI', 'UYI'), ('DZD', 'DZD'), ('YUD', 'YUD'), ('GWE', 'GWE'), ('ALL', 'ALL'), ('XBA', 'XBA'), ('BEC', 'BEC'), ('BGN', 'BGN'), ('PTE', 'PTE'), ('TJR', 'TJR'), ('CDF', 'CDF'), ('XOF', 'XOF'), ('BRC', 'BRC'), ('BOP', 'BOP'), ('BIF', 'BIF'), ('KES', 'KES'), ('BGL', 'BGL'), ('CHW', 'CHW'), ('BGO', 'BGO'), ('XFU', 'XFU'), ('AOA', 'AOA'), ('NLG', 'NLG'), ('CRC', 'CRC'), ('SSP', 'SSP'), ('XFO', 'XFO'), ('INR', 'INR'), ('USD', 'USD'), ('BRR', 'BRR'), ('MUR', 'MUR'), ('ZRZ', 'ZRZ'), ('MCF', 'MCF'), ('MVP', 'MVP'), ('MZN', 'MZN'), ('MYR', 'MYR'), ('BOV', 'BOV'), ('UYP', 'UYP'), ('KWD', 'KWD'), ('MXN', 'MXN'), ('SGD', 'SGD'), ('LKR', 'LKR'), ('XRE', 'XRE'), ('CLE', 'CLE'), ('MGA', 'MGA'), ('YER', 'YER'), ('YUM', 'YUM'), ('SLE', 'SLE'), ('ROL', 'ROL'), ('UYU', 'UYU'), ('BRL', 'BRL'), ('MRO', 'MRO'), ('SHP', 'SHP'), ('JMD', 'JMD'), ('SDD', 'SDD'), ('GYD', 'GYD'), ('ILS', 'ILS'), ('UZS', 'UZS'), ('MMK', 'MMK'), ('AED', 'AED'), ('GQE', 'GQE'), ('THB', 'THB'), ('RUR', 'RUR'), ('DDM', 'DDM'), ('XBC', 'XBC'), ('NZD', 'NZD'), ('XPD', 'XPD'), ('USN', 'USN'), ('XUA', 'XUA'), ('AUD', 'AUD'), ('ATS', 'ATS'), ('PYG', 'PYG'), ('BOL', 'BOL'), ('VED', 'VED'), ('IEP', 'IEP'), ('RWF', 'RWF'), ('PKR', 'PKR'), ('PLN', 'PLN'), ('AFN', 'AFN'), ('CNH', 'CNH'), ('EEK', 'EEK'), ('SKK', 'SKK'), ('BMD', 'BMD'), ('NIC', 'NIC'), ('ISJ', 'ISJ'), ('BGM', 'BGM'), ('ILR', 'ILR'), ('TMT', 'TMT'), ('BEF', 'BEF'), ('CHE', 'CHE'), ('TWD', 'TWD'), ('MGF', 'MGF'), ('NGN', 'NGN'), ('ANG', 'ANG'), ('FIM', 'FIM'), ('XAG', 'XAG'), ('ARP', 'ARP'), ('NPR', 'NPR'), ('KRO', 'KRO'), ('CVE', 'CVE'), ('CUP', 'CUP'), ('ECV', 'ECV'), ('CUC', 'CUC'), ('PES', 'PES'), ('ITL', 'ITL'), ('HRD', 'HRD'), ('QAR', 'QAR'), ('NAD', 'NAD'), ('UYW', 'UYW'), ('EGP', 'EGP'), ('TZS', 'TZS'), ('TRL', 'TRL'), ('DJF', 'DJF'), ('SVC', 'SVC'), ('BYB', 'BYB'), ('FJD', 'FJD'), ('DEM', 'DEM'), ('IDR', 'IDR'), ('XEU', 'XEU'), ('BYR', 'BYR'), ('LUF', 'LUF'), ('KHR', 'KHR'), ('BRB', 'BRB'), ('TND', 'TND'), ('BEL', 'BEL'), ('BAD', 'BAD'), ('BTN', 'BTN'), ('GEL', 'GEL'), ('VES', 'VES'), ('KPW', 'KPW'), ('ARL', 'ARL'), ('MOP', 'MOP'), ('LVL', 'LVL'), ('GHS', 'GHS'), ('ADP', 'ADP'), ('ZAR', 'ZAR'), ('SRD', 'SRD'), ('RHD', 'RHD'), ('XPT', 'XPT'), ('SRG', 'SRG'), ('KGS', 'KGS'), ('BND', 'BND'), ('IQD', 'IQD'), ('BBD', 'BBD'), ('BRZ', 'BRZ'), ('AMD', 'AMD'), ('AFA', 'AFA'), ('SDG', 'SDG'), ('SEK', 'SEK'), ('MWK', 'MWK'), ('ZAL', 'ZAL'), ('ARM', 'ARM'), ('KRH', 'KRH'), ('TJS', 'TJS'), ('MZE', 'MZE'), ('BHD', 'BHD'), ('TOP', 'TOP'), ('USS', 'USS'), ('HNL', 'HNL'), ('BWP', 'BWP'), ('VEF', 'VEF'), ('ARS', 'ARS'), ('MDL', 'MDL'), ('TTD', 'TTD'), ('CSD', 'CSD'), ('PHP', 'PHP'), ('LTL', 'LTL'), ('SCR', 'SCR'), ('CLP', 'CLP'), ('ETB', 'ETB'), ('GBP', 'GBP'), ('CLF', 'CLF'), ('XAF', 'XAF'), ('BDT', 'BDT'), ('SAR', 'SAR'), ('EUR', 'EUR'), ('NIO', 'NIO'), ('SDP', 'SDP'), ('IRR', 'IRR'), ('ARA', 'ARA'), ('CYP', 'CYP'), ('LBP', 'LBP'), ('MDC', 'MDC'), ('VEB', 'VEB'), ('LYD', 'LYD'), ('SOS', 'SOS'), ('SIT', 'SIT'), ('FKP', 'FKP'), ('VNN', 'VNN'), ('YUN', 'YUN'), ('UGX', 'UGX'), ('XBD', 'XBD'), ('XCD', 'XCD'), ('KRW', 'KRW'), ('CNY', 'CNY'), ('SBD', 'SBD'), ('UAK', 'UAK'), ('BUK', 'BUK'), ('STN', 'STN'), ('PEN', 'PEN'), ('GNF', 'GNF'), ('GHC', 'GHC'), ('XXX', 'XXX'), ('LUC', 'LUC'), ('GNS', 'GNS'), ('MRU', 'MRU'), ('UGS', 'UGS'), ('RSD', 'RSD'), ('HKD', 'HKD'), ('SYP', 'SYP'), ('MKN', 'MKN'), ('YUR', 'YUR'), ('GWP', 'GWP'), ('ZWL', 'ZWL'), ('AON', 'AON'), ('ESA', 'ESA'), ('HUF', 'HUF'), ('TRY', 'TRY'), ('PGK', 'PGK'), ('GIP', 'GIP'), ('GEK', 'GEK'), ('ZWD', 'ZWD'), ('CSK', 'CSK'), ('XTS', 'XTS'), ('ZMK', 'ZMK'), ('MTP', 'MTP'), ('VUV', 'VUV'), ('GMD', 'GMD'), ('LAK', 'LAK'), ('MAF', 'MAF'), ('VND', 'VND'), ('AOR', 'AOR'), ('ERN', 'ERN'), ('PEI', 'PEI'), ('BRN', 'BRN'), ('ZMW', 'ZMW'), ('STD', 'STD'), ('XSU', 'XSU'), ('BAM', 'BAM'), ('COP', 'COP'), ('MKD', 'MKD'), ('AOK', 'AOK'), ('CZK', 'CZK'), ('ECS', 'ECS'), ('NOK', 'NOK'), ('XDR', 'XDR'), ('ILP', 'ILP'), ('UAH', 'UAH'), ('MXV', 'MXV'), ('TPE', 'TPE'), ('ZRN', 'ZRN'), ('MXP', 'MXP'), ('PLZ', 'PLZ'), ('ISK', 'ISK'), ('ZWR', 'ZWR'), ('LVR', 'LVR'), ('ESB', 'ESB'), ('COU', 'COU'), ('HTG', 'HTG'), ('AWG', 'AWG'), ('FRF', 'FRF'), ('SZL', 'SZL'), ('HRK', 'HRK'), ('BYN', 'BYN'), ('ESP', 'ESP')], default='USD', max_length=3)),
                ('reset_day', models.IntegerField(default='1', max_length=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]