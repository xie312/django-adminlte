# Generated by Django 2.2.10 on 2020-08-11 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FieldTesting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_testing_id', models.FloatField(blank=True, null=True)),
                ('study_code_id', models.FloatField(blank=True, null=True)),
                ('category_code_id', models.FloatField(blank=True, null=True)),
                ('field_year', models.FloatField(blank=True, null=True)),
                ('test_location_code_id', models.FloatField(blank=True, null=True)),
                ('tpt_id_key', models.CharField(blank=True, max_length=5000, null=True)),
                ('source_type', models.CharField(blank=True, max_length=5000, null=True)),
                ('source_type_code_id', models.FloatField(blank=True, null=True)),
                ('tpt_public_flag', models.CharField(blank=True, max_length=5000, null=True)),
                ('field_testing_type', models.FloatField(blank=True, null=True)),
                ('field_testing_type_code_id', models.FloatField(blank=True, null=True)),
                ('product_phase_code_id', models.FloatField(blank=True, null=True)),
                ('field_altitude', models.FloatField(blank=True, null=True)),
                ('planned_application_intervals', models.CharField(blank=True, max_length=5000, null=True)),
                ('plot_area_assessed', models.FloatField(blank=True, null=True)),
                ('soil_cation_exchange_capacity', models.FloatField(blank=True, null=True)),
                ('field_city', models.CharField(blank=True, max_length=5000, null=True)),
                ('cost_account', models.CharField(blank=True, max_length=5000, null=True)),
                ('cost_comment', models.CharField(blank=True, max_length=5000, null=True)),
                ('cost_external', models.FloatField(blank=True, null=True)),
                ('cost_factor', models.FloatField(blank=True, null=True)),
                ('cost_internal', models.FloatField(blank=True, null=True)),
                ('cost_percent_proportion', models.FloatField(blank=True, null=True)),
                ('cost_time', models.FloatField(blank=True, null=True)),
                ('costs_identification', models.CharField(blank=True, max_length=5000, null=True)),
                ('costs_tdno', models.CharField(blank=True, max_length=5000, null=True)),
                ('field_country_code_id', models.FloatField(blank=True, null=True)),
                ('field_county', models.CharField(blank=True, max_length=5000, null=True)),
                ('currency_code_id', models.FloatField(blank=True, null=True)),
                ('data_deadline', models.DateTimeField(blank=True, null=True)),
                ('experimental_season_code_id', models.FloatField(blank=True, null=True)),
                ('external_number', models.CharField(blank=True, max_length=5000, null=True)),
                ('field_name', models.CharField(blank=True, max_length=5000, null=True)),
                ('initiation_date', models.DateTimeField(blank=True, null=True)),
                ('last_ass_changes', models.DateTimeField(blank=True, null=True)),
                ('last_dbupdate_date', models.DateTimeField(blank=True, null=True)),
                ('last_ede_update_date', models.DateTimeField(blank=True, null=True)),
                ('last_visit_date', models.DateTimeField(blank=True, null=True)),
                ('field_latitude', models.CharField(blank=True, max_length=5000, null=True)),
                ('field_longitude', models.CharField(blank=True, max_length=5000, null=True)),
                ('field_map_reference', models.CharField(blank=True, max_length=5000, null=True)),
                ('met_stat_closest', models.CharField(blank=True, max_length=5000, null=True)),
                ('met_stat_distance', models.FloatField(blank=True, null=True)),
                ('met_stat_distance_unit_code_id', models.FloatField(blank=True, null=True)),
                ('met_stat_flag', models.CharField(blank=True, max_length=5000, null=True)),
                ('no_replicates', models.FloatField(blank=True, null=True)),
                ('no_treatments', models.FloatField(blank=True, null=True)),
                ('planned_no_applications', models.CharField(blank=True, max_length=5000, null=True)),
                ('planned_no_assessments', models.FloatField(blank=True, null=True)),
                ('planned_no_harvest', models.FloatField(blank=True, null=True)),
                ('no_plots', models.FloatField(blank=True, null=True)),
                ('planned_total_no_trials', models.CharField(blank=True, max_length=5000, null=True)),
                ('field_orientation', models.FloatField(blank=True, null=True)),
                ('overall_moist_condition_code_id', models.FloatField(blank=True, null=True)),
                ('soil_percent_carbon', models.FloatField(blank=True, null=True)),
                ('soil_percent_clay', models.FloatField(blank=True, null=True)),
                ('soil_percent_gravel', models.FloatField(blank=True, null=True)),
                ('soil_percent_organic_matter', models.FloatField(blank=True, null=True)),
                ('soil_percent_sand', models.FloatField(blank=True, null=True)),
                ('soil_percent_silt', models.FloatField(blank=True, null=True)),
                ('soil_percent_lime', models.FloatField(blank=True, null=True)),
                ('plot_area', models.FloatField(blank=True, null=True)),
                ('plot_area_unit_code_id', models.FloatField(blank=True, null=True)),
                ('plot_description', models.FloatField(blank=True, null=True)),
                ('plot_description_basis_code_id', models.FloatField(blank=True, null=True)),
                ('plot_length', models.FloatField(blank=True, null=True)),
                ('plot_width', models.FloatField(blank=True, null=True)),
                ('plot_wl_unit_code_id', models.FloatField(blank=True, null=True)),
                ('prot_edition_number', models.FloatField(blank=True, null=True)),
                ('purpose', models.CharField(blank=True, max_length=5000, null=True)),
                ('quality_code_id', models.FloatField(blank=True, null=True)),
                ('quality_met_code_id', models.FloatField(blank=True, null=True)),
                ('site_type_code_id', models.FloatField(blank=True, null=True)),
                ('slope_code_id', models.FloatField(blank=True, null=True)),
                ('soil_drainage_code_id', models.FloatField(blank=True, null=True)),
                ('soil_name', models.CharField(blank=True, max_length=5000, null=True)),
                ('soil_ph', models.FloatField(blank=True, null=True)),
                ('soil_quality_number', models.FloatField(blank=True, null=True)),
                ('soil_texture_code_id', models.FloatField(blank=True, null=True)),
                ('field_state', models.CharField(blank=True, max_length=5000, null=True)),
                ('status_code_id', models.FloatField(blank=True, null=True)),
                ('status_date', models.DateTimeField(blank=True, null=True)),
                ('status_last_update_by', models.CharField(blank=True, max_length=5000, null=True)),
                ('test_type', models.CharField(blank=True, max_length=5000, null=True)),
                ('tillage_type_code_id', models.FloatField(blank=True, null=True)),
                ('title1', models.CharField(blank=True, max_length=5000, null=True)),
                ('title2', models.CharField(blank=True, max_length=5000, null=True)),
                ('plot_area_treated', models.FloatField(blank=True, null=True)),
                ('trial_design_code_id', models.FloatField(blank=True, null=True)),
                ('stat_design_code_id', models.FloatField(blank=True, null=True)),
                ('fertility_level_code_id', models.FloatField(blank=True, null=True)),
                ('control_field_code_id', models.FloatField(blank=True, null=True)),
                ('set_no_factors', models.FloatField(blank=True, null=True)),
                ('set_no_plots', models.FloatField(blank=True, null=True)),
                ('set_no_repl', models.FloatField(blank=True, null=True)),
                ('field_zip_code', models.CharField(blank=True, max_length=5000, null=True)),
                ('creation_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('ass_date_deadline_flag', models.CharField(blank=True, max_length=5000, null=True)),
                ('buffer_zone', models.CharField(blank=True, max_length=5000, null=True)),
                ('planned_started_date', models.DateTimeField(blank=True, null=True)),
                ('site_description_view', models.CharField(blank=True, max_length=5000, null=True)),
                ('plot_description_view', models.CharField(blank=True, max_length=5000, null=True)),
                ('trtm_description_view', models.CharField(blank=True, max_length=5000, null=True)),
                ('tpt_editor', models.CharField(blank=True, max_length=5000, null=True)),
                ('protocol_editor', models.CharField(blank=True, max_length=5000, null=True)),
                ('first_crop_objects_id', models.FloatField(blank=True, null=True)),
                ('previous_crop_objects_id', models.FloatField(blank=True, null=True)),
                ('first_appl_date', models.DateTimeField(blank=True, null=True)),
                ('last_appl_date', models.DateTimeField(blank=True, null=True)),
                ('first_ass_date', models.DateTimeField(blank=True, null=True)),
                ('last_ass_date', models.DateTimeField(blank=True, null=True)),
                ('planned_total_no_trials_no', models.FloatField(blank=True, null=True)),
                ('tpt_editor_cwid', models.CharField(blank=True, max_length=5000, null=True)),
                ('field_latitude_ll', models.FloatField(blank=True, null=True)),
                ('field_latitude_ul', models.FloatField(blank=True, null=True)),
                ('field_latitude_ur', models.FloatField(blank=True, null=True)),
                ('field_latitude_lr', models.FloatField(blank=True, null=True)),
                ('field_longitude_ll', models.FloatField(blank=True, null=True)),
                ('field_longitude_ul', models.FloatField(blank=True, null=True)),
                ('field_longitude_ur', models.FloatField(blank=True, null=True)),
                ('field_longitude_lr', models.FloatField(blank=True, null=True)),
                ('tptgroup_code_id', models.FloatField(blank=True, null=True)),
                ('weather_station_code_id', models.FloatField(blank=True, null=True)),
                ('water_leaching', models.FloatField(blank=True, null=True)),
                ('water_leaching_unit_code_id', models.FloatField(blank=True, null=True)),
                ('interim_due_date', models.DateTimeField(blank=True, null=True)),
                ('gep_certification', models.CharField(blank=True, max_length=5000, null=True)),
                ('internal_value', models.CharField(blank=True, max_length=5000, null=True)),
                ('compliance_code_id', models.FloatField(blank=True, null=True)),
                ('text_compliance_code_id', models.FloatField(blank=True, null=True)),
                ('phenotyping_data_flag', models.CharField(blank=True, max_length=5000, null=True)),
                ('gep_code_id', models.FloatField(blank=True, null=True)),
                ('harvest_dest_done_code_id', models.FloatField(blank=True, null=True)),
                ('harvest_dest_comment', models.CharField(blank=True, max_length=5000, null=True)),
                ('harvest_dest_method_code_id', models.FloatField(blank=True, null=True)),
                ('harvest_dest_name', models.CharField(blank=True, max_length=5000, null=True)),
                ('harvest_dest_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'field_testing',
                'managed': False,
            },
        ),
    ]
