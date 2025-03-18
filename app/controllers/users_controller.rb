class UsersController < ApplicationController
  skip_before_action :verify_authenticity_token, if: -> { !request.form_data? }
  allow_unauthenticated_access only: %i[ create ]
  before_action :set_user, only: %i[ show update destroy ]
  wrap_parameters :user, include: [:email_address, :password, :password_confirmation, :name, :cpf, :phone]

  def create
    if user_params[:password] != user_params[:password_confirmation]
      return render json: { errors: ['Password and password confirmation do not match'] }, status: :bad_request
    end

    @user = User.new(user_params)
    if @user.save
      return render json: @user, status: :created
    else
      return render json: { errors: @user.errors.full_messages }, status: :bad_request
    end
  end

  def index
    @users = User.all
    render json: @users
  end

  def show
    render json: @user
  end

  def update
    if @user.update(user_params)
      return render json: @user, status: :ok
    else
      return render json: { errors: @user.errors.full_messages }, status: :bad_request
    end
  end

  def destroy
    if @user.destroy
      return render json: {}, status: :no_content
    else
      return render json: { errors: @user.errors.full_messages }, status: :bad_request
    end
  end

  private
  def set_user
    begin
      @user = User.find(params[:id])
    rescue ActiveRecord::RecordNotFound => error
      return render json: { errors: [error.message] }, status: :not_found
    end
  end

  def user_params
    params.require(:user).permit(:email_address, :password, :password_confirmation, :name, :cpf, :phone)
  end
end
