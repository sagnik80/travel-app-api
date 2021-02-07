# Generated by Django 3.1.5 on 2021-01-29 18:24

from django.db import migrations, models # type: ignore


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientid', models.UUIDField(blank=True, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('ethnicity', models.TextField(blank=True, null=True)),
                ('deceaseddate', models.DateField(blank=True, null=True)),
                ('isdeceased', models.BooleanField(blank=True, null=True)),
                ('vitalstatus', models.TextField(blank=True, null=True)),
                ('race', models.TextField(blank=True, null=True)),
                ('sex', models.TextField(blank=True, null=True)),
                ('sourcename', models.CharField(blank=True, max_length=64, null=True)),
                ('tumor_diagnosisdate', models.DateField(blank=True, null=True)),
                ('tumor_type', models.CharField(blank=True, max_length=1024, null=True)),
                ('tumor_histology', models.TextField(blank=True, null=True)),
                ('stage_m', models.TextField(blank=True, null=True)),
                ('stage_stagegroup', models.TextField(blank=True, null=True)),
                ('metastasis_bodysite', models.CharField(blank=True, max_length=4096, null=True)),
                ('metastasis_metastasisdate', models.DateField(blank=True, null=True)),
                ('hasmetastasis', models.BooleanField(blank=True, null=True)),
                ('procedure_proceduretype', models.CharField(blank=True, max_length=4096, null=True)),
                ('recurrence_recurrencetype', models.CharField(blank=True, max_length=4096, null=True)),
                ('familyhistory_condition', models.CharField(blank=True, max_length=4096, null=True)),
                ('familyhistory_relationship', models.TextField(blank=True, null=True)),
                ('riskfactor_menopausalvalue', models.TextField(blank=True, null=True)),
                ('riskfactor_ashkenazivalue', models.TextField(blank=True, null=True)),
                ('diagnostic_status_flag', models.IntegerField(blank=True, null=True)),
                ('molecularreport_id', models.UUIDField(blank=True, null=True)),
                ('molecularreport_labname', models.CharField(blank=True, max_length=256, null=True)),
                ('molecularreport_reportdate', models.DateField(blank=True, null=True)),
                ('molecularreport_testname', models.CharField(blank=True, max_length=256, null=True)),
                ('molecularbiomarker_platformtechnology', models.CharField(blank=True, max_length=4096, null=True)),
                ('molecularbiomarker_biomarkername', models.CharField(blank=True, max_length=4096, null=True)),
                ('molecularbiomarker_biomarkertype', models.CharField(blank=True, max_length=4096, null=True)),
                ('molecularbiomarker_call', models.CharField(blank=True, max_length=4096, null=True)),
                ('molecularbiomarker_clinicalsignificance_flag', models.IntegerField(blank=True, null=True)),
                ('molecularbiomarker_gene', models.TextField(blank=True, null=True)),
                ('molecularbiomarker_genomicsource', models.CharField(blank=True, max_length=4096, null=True)),
                ('further_testing_genomic_source', models.TextField(blank=True, null=True)),
                ('hasbiomarkerreport', models.BooleanField(blank=True, null=True)),
                ('hr_positive', models.BooleanField(blank=True, null=True)),
                ('hr_negative', models.BooleanField(blank=True, null=True)),
                ('erbb2_positive', models.BooleanField(blank=True, null=True)),
                ('erbb2_negative', models.BooleanField(blank=True, null=True)),
                ('molecularbiomarker_clinicalsignificance', models.TextField(blank=True, null=True)),
                ('germline_somatic_patient_level', models.TextField(blank=True, null=True)),
                ('germline_somatic_gene_level', models.TextField(blank=True, null=True)),
                ('molecular_subtype', models.TextField(blank=True, null=True)),
                ('diagnostic_status', models.TextField(blank=True, null=True)),
                ('molecularbiomarker_genes', models.TextField(blank=True, null=True)),
                ('targetedtherapy', models.TextField(blank=True, null=True)),
                ('lineoftherapy', models.IntegerField(blank=True, null=True)),
                ('actionable', models.BooleanField(blank=True, null=True)),
                ('genecount', models.IntegerField(blank=True, null=True)),
                ('sizecategory', models.CharField(blank=True, max_length=4096, null=True)),
                ('specificity', models.CharField(blank=True, max_length=4096, null=True)),
                ('biomarkerclass', models.CharField(blank=True, max_length=4096, null=True)),
                ('drugclass', models.TextField(blank=True, null=True)),
                ('hasactionabletargetedtherapy', models.BooleanField(blank=True, null=True)),
                ('nottargetedtherapytested', models.BooleanField(blank=True, null=True)),
                ('targeted_therapy_genes', models.TextField(blank=True, null=True)),
                ('actionable_genes', models.TextField(blank=True, null=True)),
                ('genes_tested', models.TextField(blank=True, null=True)),
                ('carecategory', models.TextField(blank=True, null=True)),
                ('molecularbiomarker_biomarkertested', models.TextField(blank=True, null=True)),
                ('targetedtherapymolecularindicator', models.TextField(blank=True, null=True)),
                ('targeted_therapy_gene', models.TextField(blank=True, null=True)),
                ('riskfactor_oncotypedxdate', models.DateField(blank=True, null=True)),
                ('riskfactor_oncotypedxvalue', models.TextField(blank=True, null=True)),
                ('riskfactor_oncotypedxinterpretation', models.TextField(blank=True, null=True)),
                ('riskfactor_oncotypedxname', models.TextField(blank=True, null=True)),
                ('suborg', models.CharField(blank=True, max_length=64, null=True)),
                ('haschemotherapy', models.BooleanField(blank=True, null=True)),
                ('chemotherapydrug', models.TextField(blank=True, null=True)),
                ('source_schema', models.CharField(blank=True, max_length=64, null=True)),
            ],
            options={
                'db_table': '"bti"."breast"',
                'managed': False,
            },
        ),
    ]