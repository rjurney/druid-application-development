# myapp.rb
require 'sinatra'
require 'druid'
require 'json'

set :public_folder, File.dirname(__FILE__) + '/static'
set :views, 'templates'

client = Druid::Client.new('', {:static_setup => { 'realtime/wikipedia' => 'http://localhost:8083/druid/v2/' }})

get '/timeseries' do
  query = Druid::Query.new('realtime/wikipedia').double_sum(:added).granularity(:minute).interval("2013-01-01", "2014-01-01")
  result = client.send(query)
  jsonable = result.map {|r| {'timestamp' => r.timestamp, 'result' => r.row}}
  @json = JSON.generate(jsonable)
  puts @json
  erb :index
end
