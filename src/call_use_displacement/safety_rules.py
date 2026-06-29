#!/usr/bin/env python3
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class SafetyDecision:
    allowed: bool
    reasons: list[str]


def decide_call_use_displacement(
    preserves_data_dependence: bool,
    preserves_anti_dependence: bool,
    preserves_output_dependence: bool,
    preserves_control_dependence: bool,
    no_unsafe_aliasing: bool,
    no_unordered_side_effects: bool,
    preserves_exception_order: bool,
    preserves_object_lifetime: bool,
    no_volatile_or_atomic_reordering: bool,
    synchronization_before_first_use: bool,
) -> SafetyDecision:
    checks = {
        'data dependence not preserved': preserves_data_dependence,
        'anti-dependence not preserved': preserves_anti_dependence,
        'output dependence not preserved': preserves_output_dependence,
        'control dependence not preserved': preserves_control_dependence,
        'unsafe pointer/reference aliasing possible': no_unsafe_aliasing,
        'side-effect ordering not guaranteed': no_unordered_side_effects,
        'exception order not preserved': preserves_exception_order,
        'object lifetime/destructor safety not guaranteed': preserves_object_lifetime,
        'volatile/atomic operation would be reordered': no_volatile_or_atomic_reordering,
        'missing synchronization before first use': synchronization_before_first_use,
    }
    failed = [reason for reason, ok in checks.items() if not ok]
    return SafetyDecision(allowed=not failed, reasons=failed)
