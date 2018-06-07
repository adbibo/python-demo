#!/usr/bin/env python
# -*- coding=utf-8 -*-

import re

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, GoogleCloudOptions, StandardOptions

options = PipelineOptions()
google_cloud_options = options.view_as(GoogleCloudOptions)
google_cloud_options.project = 'my-project-id'
google_cloud_options.job_name = 'myjob'
google_cloud_options.staging_location = 'gs://your-bucket-name-here/staging'
google_cloud_options.temp_location = 'gs://your-bucket-name-here/temp'
options.view_as(StandardOptions).runner = 'DataflowRunner'

p = beam.Pipeline(options=options)


class CountWords(beam.PTransform):
  def expand(self, pcoll):
    return (pcoll
            # Convert lines of text into individual words.
            | 'ExtractWords' >> beam.FlatMap(
                lambda x: re.findall(r'[A-Za-z\']+', x))

            # Count the number of times each word occurs.
            | beam.combiners.Count.PerElement())

counts = lines | CountWords()