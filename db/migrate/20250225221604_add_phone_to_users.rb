class AddPhoneToUsers < ActiveRecord::Migration[8.0]
  def change
    add_column :users, :phone, :integer
  end
end
