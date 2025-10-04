"""
Test to validate security requirements and dependency versions
"""
import subprocess
import sys
from packaging import version


def test_minimum_package_versions():
    """Ensure critical packages meet minimum secure versions"""
    
    # Define minimum secure versions for critical packages
    min_versions = {
        'pip': '25.2',
        'setuptools': '80.9.0',
        'requests': '2.32.5',
        'urllib3': '2.2.2',
        'jinja2': '3.1.6',
        'certifi': '2024.7.4',
        'cryptography': '43.0.1',
        'idna': '3.7'
    }
    
    # Get installed versions
    result = subprocess.run(
        [sys.executable, '-m', 'pip', 'list', '--format=json'],
        capture_output=True,
        text=True
    )
    
    import json
    installed = {pkg['name'].lower(): pkg['version'] for pkg in json.loads(result.stdout)}
    
    # Check each package
    failures = []
    for package, min_ver in min_versions.items():
        if package in installed:
            installed_ver = installed[package]
            if version.parse(installed_ver) < version.parse(min_ver):
                failures.append(
                    f"{package}: installed {installed_ver} < required {min_ver}"
                )
        else:
            failures.append(f"{package}: not installed")
    
    assert not failures, "Security version requirements not met:\n" + "\n".join(failures)


def test_pip_audit_runs_successfully():
    """Ensure pip-audit can run (even if vulnerabilities exist)"""
    result = subprocess.run(
        [sys.executable, '-m', 'pip_audit', '--version'],
        capture_output=True,
        text=True
    )
    
    assert result.returncode == 0, f"pip-audit not working: {result.stderr}"


def test_no_critical_unignored_vulnerabilities():
    """
    Ensure no critical vulnerabilities exist beyond the known/ignored ones.
    This test ignores vulnerabilities that are documented in SECURITY.md
    """
    # Known vulnerabilities that are documented and accepted
    ignored_vulns = [
        'GHSA-4xh5-x5gv-qwph',  # pip - fix not yet released
        'PYSEC-2024-75',         # twisted - system package
        'GHSA-c8m8-j448-xjx7'    # twisted - system package
    ]
    
    result = subprocess.run(
        [sys.executable, '-m', 'pip_audit'] + 
        [f'--ignore-vuln={v}' for v in ignored_vulns],
        capture_output=True,
        text=True
    )
    
    # With ignored vulnerabilities, should pass
    assert result.returncode == 0, (
        f"Unexpected vulnerabilities found:\n{result.stdout}\n{result.stderr}"
    )


if __name__ == "__main__":
    test_minimum_package_versions()
    test_pip_audit_runs_successfully()
    test_no_critical_unignored_vulnerabilities()
    print("✅ All security tests passed!")
