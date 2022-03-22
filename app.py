#!/usr/bin/env python3

import aws_cdk as cdk

from cdkpy_workshop.cdkpy_workshop_stack import CdkpyWorkshopStack


app = cdk.App()
CdkpyWorkshopStack(app, "cdkpy-workshop")

app.synth()
