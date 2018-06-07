#!/usr/bin/env python
# -*- coding=utf-8 -*-

from apache_beam.options.pipeline_options import PipelineOptions


class AdOptions(PipelineOptions):

  @classmethod
  def _add_argparse_args(cls, parser):
      parser.add_argument('--input',
                          help='Input for the pipeline',
                          default='gs://my-bucket/input')
      parser.add_argument('--output',
                          help='Output for the pipeline',
                          default='gs://my-bucket/output')

