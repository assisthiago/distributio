class AddCpfToUsers < ActiveRecord::Migration[8.0]
  def change
    add_column :users, :cpf, :integer
  end
end
