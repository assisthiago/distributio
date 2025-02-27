class ChangeIntegerLimitInUsers < ActiveRecord::Migration[8.0]
  def change
    change_column :users, :cpf, :integer, limit: 8
    change_column :users, :phone, :integer, limit: 8
  end
end
