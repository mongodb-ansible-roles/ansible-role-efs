# frozen_string_literal: true

describe mount('/efs') do
  it { should be_mounted }
  its('device') { should eq 'overlay' }
  its('type') { should eq 'overlay' }
end

describe file('/efs/test') do
  it { should exist }
end

describe command('ls /efs/*/info') do
  its('exit_status') { should eq 0 }
end

describe command('ls /efs/*/info/distro_name') do
  its('exit_status') { should eq 0 }
end

describe command('ls /efs/*/scons-cache') do
  its('exit_status') { should eq 0 }
end
